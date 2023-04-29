import io
import pprint
from re import sub

import networkx as nx
from pyvis.network import Network

from default_values import DEFAULT_VALUES
from default_values import SAI_OBJECT_TYPES

# give your custom path
SAI_CODE_LOCATION = r'/home/ubuntuserver/dinesh/SAI/'
SAI_CODE_LOCATION = r'C:/github-keysight/SAI'

TEST_TEMPLATE = '''
from pprint import pprint

import pytest


class TestSai%(CLASS_NAME)s:
    # %(COMMENT)s

    @pytest.mark.dependency(scope='session')
    def test_%(OBJECT_NAME)s_create(self, npu):

        commands = %(CREATE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_%(OBJECT_NAME)s_remove(self, npu):

        commands = %(REMOVE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'

'''


def get_object_types():
    return SAI_OBJECT_TYPES


def get_all_attributes(obj_type):
    obj_name = get_obj_name(obj_type)
    block_start = 'typedef enum _sai_%s_attr_t' % obj_name
    block_end = '} sai_%s_attr_t;' % obj_name

    dictionary = {}
    import os

    for root, dirs, files in os.walk(SAI_CODE_LOCATION):
        for file in files:
            if file.endswith('.h'):
                start_copy = False
                is_attribute = False
                attr_block_start = False
                with io.open(os.path.join(root, file), 'rt', encoding='utf-8') as h_file:
                    for text_line in h_file:
                        if block_start in text_line:
                            print(os.path.join(root, file))
                            start_copy = True
                        if block_end in text_line:
                            start_copy = False
                        if start_copy:
                            if attr_block_start:
                                if '@type' in text_line:
                                    o_type = text_line.replace('* @type', '').strip()
                                if '@flags' in text_line:
                                    flags = text_line.replace('* @flags', '').strip()
                                if '@objects' in text_line:
                                    objects = []
                                    for parent in text_line.replace('* @objects', '').strip().split(','):
                                        objects.append(parent.strip())
                                        if flags:
                                            if 'MANDATORY_ON_CREATE' in flags:
                                                G.add_edge(
                                                    obj_type.replace('SAI_OBJECT_TYPE_', ''),
                                                    parent.strip().replace('SAI_OBJECT_TYPE_', ''),
                                                )
                                if '@allownull' in text_line:
                                    allownull = text_line.replace('* @allownull', '').strip()
                                if '@default' in text_line:
                                    default = text_line.replace('* @default', '').strip()

                            if is_attribute:
                                attribute = text_line.split('=')[0].replace(',', '').strip()
                                if attribute != '':
                                    dictionary[attribute] = {}
                                    dictionary[attribute]['type'] = o_type
                                    dictionary[attribute]['flags'] = flags
                                    dictionary[attribute]['objects'] = objects
                                    dictionary[attribute]['allownull'] = allownull
                                    dictionary[attribute]['default'] = default
                                    # print(attribute)
                                    # print(dictionary[attribute])
                                o_type = None
                                flags = None
                                objects = None
                                allownull = None
                                default = None
                                is_attribute = False

                            if '/**' in text_line:
                                attr_block_start = True
                                o_type = None
                                flags = None
                                objects = None
                                allownull = None
                                default = None
                            if '*/' in text_line:
                                attr_block_start = False
                                is_attribute = True

    # pprint.pprint(dictionary)
    return dictionary


def select_mandatory_attributes(all_attributes):
    mandatory = {}
    for attribute in all_attributes.keys():
        if all_attributes[attribute]['flags'] is not None:
            if 'MANDATORY_ON_CREATE' in all_attributes[attribute]['flags']:
                mandatory[attribute] = all_attributes[attribute]

    pprint.pprint(mandatory)
    return mandatory


def get_obj_name(obj_type):
    return obj_type.replace('SAI_OBJECT_TYPE_', '').lower()


def get_create_commands(obj_type):
    obj_name = get_obj_name(obj_type)
    command = {'name': obj_name + '_1', 'op': 'create', 'type': obj_type}
    commands = []
    attributes = []
    mandatory_attributes = select_mandatory_attributes(get_all_attributes(obj_type))
    for attribute in mandatory_attributes.keys():
        attributes.append(attribute)
        if 'type' in mandatory_attributes[attribute].keys():
            attr_type = mandatory_attributes[attribute]['type']
            if attr_type in DEFAULT_VALUES.keys():
                attributes.append(DEFAULT_VALUES[attr_type])
            elif 'sai_object_id_t' == attr_type:
                parent_obj = mandatory_attributes[attribute]['objects'][0]
                if parent_obj != obj_type:
                    attributes.append('$' + get_obj_name(parent_obj) + '_1')
                    commands.extend(get_create_commands(parent_obj))
                else:
                    attributes.append('TODO_circular parent reference')
            else:
                attributes.append(attr_type)
        else:
            attributes.append('TODO')
    command['attributes'] = attributes
    commands.append(command)

    unique_commands = []
    for command in commands:
        if command not in unique_commands:
            unique_commands.append(command)

    return unique_commands


def get_remove_commands(obj_type):
    commands = get_create_commands(obj_type)
    cleanup_commands = []
    for command in reversed(commands):
        command['op'] = 'remove'
        cleanup_commands.append(command)
    return cleanup_commands


def camel_case(s):
    s = sub(r'(_|-)+', ' ', s).title().replace(' ', '')
    return s


def generate_comment(obj_type):
    mandatory_attributes = select_mandatory_attributes(get_all_attributes(obj_type))
    if len(mandatory_attributes) == 0:
        return 'object with no attributes'
    else:
        parents = []
        for attribute in mandatory_attributes.keys():
            if 'objects' in mandatory_attributes[attribute].keys():
                if mandatory_attributes[attribute]['objects'] is not None:
                    parents.extend(mandatory_attributes[attribute]['objects'])
        if len(parents) == 0:
            return 'object with no parents'
        else:
            return 'object with parent %s' % (' '.join(parents))


def generate_pyetes_test(obj_type):
    obj_name = get_obj_name(obj_type)
    test_file_name = 'test_%s.py' % obj_name
    print(test_file_name)

    with io.open(test_file_name, 'wt', encoding='ascii') as test_file:
        test_file.write(
            TEST_TEMPLATE
            % {
                'CLASS_NAME': camel_case(obj_name),
                'OBJECT_NAME': obj_name,
                'CREATE_COMMANDS': get_create_commands(obj_type),
                'REMOVE_COMMANDS': get_remove_commands(obj_type),
                'COMMENT': generate_comment(obj_type),
            }
        )


object_dict = {}
object_types = get_object_types()

G = nx.DiGraph()
nt = Network('1300px', '2500px', notebook=True)

for obj_type in object_types:
    G.add_node(obj_type.replace('SAI_OBJECT_TYPE_', ''))
    generate_pyetes_test(obj_type)

nt.from_nx(G)
nt.show('nx.html')
