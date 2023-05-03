import io
import json
import os
import pprint
import re

import networkx
from pyvis.network import Network

from default_values import DEFAULT_VALUES, SAI_OBJECT_TYPES

# give your custom path
SAI_CODE_LOCATION = r'/home/ubuntuserver/dinesh/SAI/'
SAI_CODE_LOCATION = r'C:/github-keysight/SAI'
# SAI_CODE_LOCATION = r'C:/github-mgheorghe/SAI'

TEST_TEMPLATE_GET = '''

    %(PYTEST_MARKER)s
    def test_%(ATTR_NAME)s_get(self, npu):

        commands = [
            {
                "name": "%(OBJECT_NAME)s_1",
                "op": "get",
                "type": "%(OBJECT_TYPE)s",
                "atrribute": "%(ATTRIBUTE)s"
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)
        assert results[1][0].value() == '%(EXPECTED_VALUE)s', 'Get error, expected %(EXPECTED_VALUE)s but got %%s' %%  results[1][0].value()
'''

TEST_TEMPLATE_SET = '''

    %(PYTEST_MARKER)s
    def test_%(ATTR_NAME)s_set(self, npu):

        commands = [
            {
                "name": "%(OBJECT_NAME)s_1",
                "op": "get",
                "type": "%(OBJECT_TYPE)s",
                "atrribute": ["%(ATTRIBUTE)s", '%(EXPECTED_VALUE)s']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

'''

TEST_TEMPLATE_CREATE = '''
from pprint import pprint

import pytest


class TestSai%(CLASS_NAME)s:
    # %(COMMENT)s

    def test_%(OBJECT_NAME)s_create(self, npu):

        commands = %(CREATE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

'''
TEST_TEMPLATE_REMOVE = '''

    def test_%(OBJECT_NAME)s_remove(self, npu):

        commands = %(REMOVE_COMMANDS)s

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'

'''


def get_object_types():
    # ^.*(SAI_OBJECT_TYPE_[0-9A-Za-z_]+).*$
    return SAI_OBJECT_TYPES


def get_header_files_paths():
    header_files = []
    for root, dirs, files in os.walk(SAI_CODE_LOCATION):
        for file in files:
            if file.endswith('.h'):
                header_files.append(os.path.join(root, file))
    return header_files


def parse_sai_header_files():
    dictionary = {}
    object_types = get_object_types()

    header_files_paths = get_header_files_paths()

    for obj_type in object_types:
        dictionary[obj_type] = {}
        obj_name = get_obj_name(obj_type)
        block_start = 'typedef enum _sai_%s_attr_t' % obj_name
        block_end = '} sai_%s_attr_t;' % obj_name

        for h_file_path in header_files_paths:
            start_copy = False
            is_attribute = False
            attr_block_start = False
            with io.open(h_file_path, 'rt', encoding='utf-8') as h_file:
                for text_line in h_file:
                    if block_start in text_line:
                        print(h_file_path)
                        start_copy = True
                    if block_end in text_line:
                        start_copy = False
                    if start_copy:
                        if attr_block_start:
                            if '@type' in text_line:
                                o_types = []
                                for o_type in (
                                    text_line.replace('* @type', '').strip().split(' ')
                                ):
                                    o_types.append(o_type.strip())
                            if '@flags' in text_line:
                                flags = []
                                for flag in text_line.replace('* @flags', '').split(
                                    '|'
                                ):
                                    flags.append(flag.strip())
                            if '@objects' in text_line:
                                objects = []
                                for parent in text_line.replace('* @objects', '').split(
                                    ','
                                ):
                                    objects.append(parent.strip())
                            if '@allownull' in text_line:
                                allownull = text_line.replace(
                                    '* @allownull', ''
                                ).strip()
                            if '@default' in text_line:
                                default = text_line.replace('* @default', '').strip()

                        if is_attribute:
                            attribute = text_line.split('=')[0].replace(',', '').strip()
                            if attribute != '':
                                dictionary[obj_type][attribute] = {}
                                dictionary[obj_type][attribute]['type'] = o_type
                                dictionary[obj_type][attribute]['flags'] = flags
                                dictionary[obj_type][attribute]['objects'] = objects
                                dictionary[obj_type][attribute]['allownull'] = allownull
                                dictionary[obj_type][attribute]['default'] = default
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


def select_mandatory_attributes(obj_type):
    mandatory = {}
    for attribute in SAI_DATA[obj_type].keys():
        if SAI_DATA[obj_type][attribute]['flags'] is not None:
            if 'MANDATORY_ON_CREATE' in SAI_DATA[obj_type][attribute]['flags']:
                mandatory[attribute] = SAI_DATA[obj_type][attribute]

    pprint.pprint(mandatory)
    return mandatory


def get_obj_name(obj_type):
    return obj_type.replace('SAI_OBJECT_TYPE_', '').lower()


def get_create_commands(obj_type):
    obj_name = get_obj_name(obj_type)
    command = {'name': obj_name + '_1', 'op': 'create', 'type': obj_type}
    commands = []
    attributes = []
    mandatory_attributes = select_mandatory_attributes(obj_type)
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
    s = re.sub(r'(_|-)+', ' ', s).title().replace(' ', '')
    return s


def generate_comment(obj_type):
    mandatory_attributes = select_mandatory_attributes(obj_type)
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


def get_attribute_expected_value(attribute):
    if attribute['default'] is not None:
        return attribute['default']
    else:
        return 'TODO'


def generate_pyetes_test(obj_type):
    obj_name = get_obj_name(obj_type)
    test_file_name = 'test_%s.py' % obj_name
    # print(test_file_name)

    with io.open('generated/' + test_file_name, 'wt', encoding='ascii') as test_file:
        TEST_CODE = ''

        TEST_CODE += TEST_TEMPLATE_CREATE % {
            'CLASS_NAME': camel_case(obj_name),
            'OBJECT_NAME': obj_name,
            'CREATE_COMMANDS': get_create_commands(obj_type),
            'COMMENT': generate_comment(obj_type),
        }
        obj = SAI_DATA[obj_type]
        for attribute in SAI_DATA[obj_type].keys():
            if obj[attribute]['flags'] is not None:
                if 'READ_ONLY' in obj[attribute]['flags']:
                    TEST_CODE += TEST_TEMPLATE_GET % {
                        'PYTEST_MARKER': '',
                        'ATTR_NAME': get_obj_name(attribute),
                        'OBJECT_NAME': obj_name,
                        'OBJECT_TYPE': obj_type,
                        'ATTRIBUTE': attribute,
                        'EXPECTED_VALUE': get_attribute_expected_value(obj[attribute]),
                    }
                elif 'CREATE_AND_SET' in obj[attribute]['flags']:
                    TEST_CODE += TEST_TEMPLATE_SET % {
                        'PYTEST_MARKER': '@pytest.mark.dependency()',
                        'ATTR_NAME': get_obj_name(attribute),
                        'OBJECT_NAME': obj_name,
                        'OBJECT_TYPE': obj_type,
                        'ATTRIBUTE': attribute,
                        'EXPECTED_VALUE': get_attribute_expected_value(obj[attribute]),
                    }
                    TEST_CODE += TEST_TEMPLATE_GET % {
                        'PYTEST_MARKER': '@pytest.mark.dependency(depends=["test_%s_set"])'
                        % get_obj_name(attribute),
                        'ATTR_NAME': get_obj_name(attribute),
                        'OBJECT_NAME': obj_name,
                        'OBJECT_TYPE': obj_type,
                        'ATTRIBUTE': attribute,
                        'EXPECTED_VALUE': get_attribute_expected_value(obj[attribute]),
                    }
                else:
                    # TODO: see if any other case that can be tested exists
                    pass

        TEST_CODE += TEST_TEMPLATE_REMOVE % {
            'OBJECT_NAME': obj_name,
            'REMOVE_COMMANDS': get_remove_commands(obj_type),
        }

        test_file.write(TEST_CODE)


def create_depedency_graph():
    G = networkx.DiGraph()
    nt = Network('1300px', '2500px', notebook=True, directed=True)
    for obj_type in SAI_DATA.keys():
        obj = SAI_DATA[obj_type]
        G.add_node(obj_type.replace('SAI_OBJECT_TYPE_', ''))
        for attribute in obj.keys():
            flags = obj[attribute]['flags']
            if flags is not None:
                if 'MANDATORY_ON_CREATE' in flags:
                    objects = obj[attribute]['objects']
                    if objects is not None:
                        node1 = obj_type.replace('SAI_OBJECT_TYPE_', '')
                        node2 = obj[attribute]['objects'][0].replace(
                            'SAI_OBJECT_TYPE_', ''
                        )
                        if node1 == node2:
                            node2 = obj[attribute]['objects'][1].replace(
                                'SAI_OBJECT_TYPE_', ''
                            )
                        G.add_edge(node1, node2)

    nt.from_nx(G)
    nt.show('nx.html')


SAI_DATA = parse_sai_header_files()

with io.open('sai_api_structure.json', 'wt', encoding='ascii') as json_f:
    json.dump(SAI_DATA, json_f, indent=2)

create_depedency_graph()

for obj_type in SAI_DATA.keys():
    generate_pyetes_test(obj_type)
