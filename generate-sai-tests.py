import io
import json
import os
import pprint
import re

import networkx
from pyvis.network import Network

from default_values import DEFAULT_VALUES, SAI_OBJECT_TYPES

# give your custom path
SAI_CODE_LOCATION = r'C:\Work\products\generatesai\SAI'
# SAI_CODE_LOCATION = r'C:/github-keysight/SAI'
# SAI_CODE_LOCATION = r'C:/github-mgheorghe/SAI'

TEST_TEMPLATE_GET = '''

    %(PYTEST_MARKER)s
    def test_%(ATTR_NAME)s_get(self, %(NPU_DPU_MARKER)s):

        commands = [
            {
                "name": "%(OBJECT_NAME)s_1",
                "op": "get",
                "attributes": ["%(ATTRIBUTE)s"]
            }
        ]
        results = [*%(NPU_DPU_MARKER)s.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '%(EXPECTED_VALUE)s', 'Get error, expected %(EXPECTED_VALUE)s but got %%s' %%  r_value
'''

TEST_TEMPLATE_SET = '''

    %(PYTEST_MARKER)s
    def test_%(ATTR_NAME)s_set(self, %(NPU_DPU_MARKER)s):

        commands = [
            {
                "name": "%(OBJECT_NAME)s_1",
                "op": "set",
                "attributes": ["%(ATTRIBUTE)s", '%(EXPECTED_VALUE)s']
            }
        ]
        results = [*%(NPU_DPU_MARKER)s.process_commands(commands)]
        print("======= SAI commands RETURN values set =======")
        pprint(results)

'''

TEST_TEMPLATE_CREATE = '''
from pprint import pprint

import pytest

@pytest.fixture(scope="module", autouse=True)
def discovery(%(NPU_DPU_MARKER)s):
    %(NPU_DPU_MARKER)s.objects_discovery()

@pytest.fixture(scope="module", autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.%(NPU_DPU_MARKER)s) != 1:
        pytest.skip("invalid for {} testbed".format(testbed.name))

@pytest.mark.%(NPU_DPU_MARKER)s
class TestSai%(CLASS_NAME)s:
    # %(COMMENT)s

    def test_%(OBJECT_NAME)s_create(self, %(NPU_DPU_MARKER)s):

        commands = %(CREATE_COMMANDS)s

        results = [*%(NPU_DPU_MARKER)s.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

'''
TEST_TEMPLATE_REMOVE = '''

    def test_%(OBJECT_NAME)s_remove(self, %(NPU_DPU_MARKER)s):

        commands = %(REMOVE_COMMANDS)s

        results = [*%(NPU_DPU_MARKER)s.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

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
        dictionary[obj_type]['keys'] = {}
        dictionary[obj_type]['attributes'] = {}
        dictionary[obj_type]['npu_dpu'] = ''
        obj_name = get_obj_name(obj_type)
        attributes_block_start = 'typedef enum _sai_%s_attr_t' % obj_name
        attributes_block_end = '} sai_%s_attr_t;' % obj_name

        keys_block_start = 'typedef struct _sai_%s_t' % obj_name
        keys_block_end = '} sai_%s_t;' % obj_name

        for h_file_path in header_files_paths:
            start_copy = False
            is_attribute = False
            is_key = False
            attr_attributes_block_start = False
            parsing_attributes = False
            parsing_keys = False

            with io.open(h_file_path, 'rt', encoding='utf-8') as h_file:
                print(h_file_path)
                for text_line in h_file:
                    # print(h_file_path
                    if attributes_block_start in text_line:
                        if 'experimental' in h_file_path:
                            # temp_list.append('dpu')
                            dictionary[obj_type]['npu_dpu'] = 'dpu'
                            # break
                        else:
                            # temp_list.append('npu')
                            dictionary[obj_type]['npu_dpu'] = 'npu'
                        start_copy = True
                        parsing_attributes = True
                    if attributes_block_end in text_line:
                        start_copy = False
                        parsing_attributes = False
                    if keys_block_start in text_line:
                        # print(h_file_path)
                        start_copy = True
                        parsing_keys = True
                    if keys_block_end in text_line:
                        start_copy = False
                        parsing_keys = False
                    if start_copy:
                        if attr_attributes_block_start:
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
                                dictionary[obj_type]['attributes'][attribute] = {}
                                dictionary[obj_type]['attributes'][attribute][
                                    'type'
                                ] = o_type
                                dictionary[obj_type]['attributes'][attribute][
                                    'flags'
                                ] = flags
                                dictionary[obj_type]['attributes'][attribute][
                                    'objects'
                                ] = objects
                                dictionary[obj_type]['attributes'][attribute][
                                    'allownull'
                                ] = allownull
                                dictionary[obj_type]['attributes'][attribute][
                                    'default'
                                ] = default
                                # print(attribute)
                                # print(dictionary[attribute])
                            o_type = None
                            flags = None
                            objects = None
                            allownull = None
                            default = None
                            is_attribute = False

                        if is_key:
                            key = text_line.strip().split(' ')[1].replace(';', '')
                            if key != '':
                                dictionary[obj_type]['keys'][key] = {}
                                dictionary[obj_type]['keys'][key]['type'] = o_type
                                dictionary[obj_type]['keys'][key]['flags'] = flags
                                dictionary[obj_type]['keys'][key]['objects'] = objects
                                dictionary[obj_type]['keys'][key][
                                    'allownull'
                                ] = allownull
                                dictionary[obj_type]['keys'][key]['default'] = default
                                # print(attribute)
                                # print(dictionary[attribute])
                            o_type = None
                            flags = None
                            objects = None
                            allownull = None
                            default = None
                            is_key = False

                        if '/**' in text_line:
                            attr_attributes_block_start = True
                            o_type = None
                            flags = None
                            objects = None
                            allownull = None
                            default = None
                        if '*/' in text_line:
                            attr_attributes_block_start = False
                            if parsing_attributes:
                                is_attribute = True
                            elif parsing_keys:
                                is_key = True

    return dictionary


def select_mandatory_attributes(obj_type):
    mandatory = {}
    for attribute in SAI_DATA[obj_type]['attributes'].keys():
        if SAI_DATA[obj_type]['attributes'][attribute]['flags'] is not None:
            if (
                'MANDATORY_ON_CREATE'
                in SAI_DATA[obj_type]['attributes'][attribute]['flags']
            ):
                mandatory[attribute] = SAI_DATA[obj_type]['attributes'][attribute]

    pprint.pprint(mandatory)
    return mandatory


def get_obj_name(obj_type):
    return obj_type.replace('SAI_OBJECT_TYPE_', '').lower()


def get_obj_keys(obj_type):
    keys = {}
    for key in SAI_DATA[obj_type]['keys'].keys():
        if key == 'switch_id':
            keys[key] = '$SWITCH_ID'
        else:
            keys[key] = 'TODO'
    return keys


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
    if SAI_DATA[obj_type]['keys'] != {}:
        command['key'] = get_obj_keys(obj_type)
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
        if command['op'] == 'create':
            if 'key' in command.keys():
                cleanup_commands.append(
                    {
                        'name': command.get('name'),
                        'key': command.get('key'),
                        'op': 'remove',
                    }
                )
            else:
                cleanup_commands.append({'name': command.get('name'), 'op': 'remove'})
    return cleanup_commands
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
        return attribute['default'].replace('attrvalue', '').strip()
    else:
        return 'TODO'


def generate_pyetes_test(obj_type):
    obj_name = get_obj_name(obj_type)
    test_file_name = 'test_%s.py' % obj_name
    # print(test_file_name)

    with io.open('generated/' + test_file_name, 'wt', encoding='ascii') as test_file:
        TEST_CODE = ''

        TEST_CODE += TEST_TEMPLATE_CREATE % {
            'NPU_DPU_MARKER': SAI_DATA[obj_type]['npu_dpu'],
            'CLASS_NAME': camel_case(obj_name),
            'OBJECT_NAME': obj_name,
            'CREATE_COMMANDS': get_create_commands(obj_type),
            'COMMENT': generate_comment(obj_type),
        }
        obj = SAI_DATA[obj_type]
        for attribute in SAI_DATA[obj_type]['attributes'].keys():
            if obj['attributes'][attribute]['flags'] is not None:
                if 'READ_ONLY' in obj['attributes'][attribute]['flags']:
                    TEST_CODE += TEST_TEMPLATE_GET % {
                        'NPU_DPU_MARKER': SAI_DATA[obj_type]['npu_dpu'],
                        'PYTEST_MARKER': '',
                        'ATTR_NAME': get_obj_name(attribute),
                        'OBJECT_NAME': obj_name,
                        'OBJECT_TYPE': obj_type,
                        'ATTRIBUTE': attribute,
                        'EXPECTED_VALUE': get_attribute_expected_value(
                            obj['attributes'][attribute]
                        ),
                    }
                elif 'CREATE_AND_SET' in obj['attributes'][attribute]['flags']:
                    TEST_CODE += TEST_TEMPLATE_SET % {
                        'NPU_DPU_MARKER': SAI_DATA[obj_type]['npu_dpu'],
                        'PYTEST_MARKER': '@pytest.mark.dependency(name="test_%s_set")'
                        % get_obj_name(attribute),
                        'ATTR_NAME': get_obj_name(attribute),
                        'OBJECT_NAME': obj_name,
                        'ATTRIBUTE': attribute,
                        'EXPECTED_VALUE': get_attribute_expected_value(
                            obj['attributes'][attribute]
                        ),
                    }
                    TEST_CODE += TEST_TEMPLATE_GET % {
                        'NPU_DPU_MARKER': SAI_DATA[obj_type]['npu_dpu'],
                        'PYTEST_MARKER': '@pytest.mark.dependency(depends=["test_%s_set"])'
                        % get_obj_name(attribute),
                        'ATTR_NAME': get_obj_name(attribute),
                        'OBJECT_NAME': obj_name,
                        'OBJECT_TYPE': obj_type,
                        'ATTRIBUTE': attribute,
                        'EXPECTED_VALUE': get_attribute_expected_value(
                            obj['attributes'][attribute]
                        ),
                    }
                else:
                    # TODO: see if any other case that can be tested exists
                    pass

        TEST_CODE += TEST_TEMPLATE_REMOVE % {
            'NPU_DPU_MARKER': SAI_DATA[obj_type]['npu_dpu'],
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
        for attribute in obj['attributes'].keys():
            flags = obj['attributes'][attribute]['flags']
            if flags is not None:
                if 'MANDATORY_ON_CREATE' in flags:
                    objects = obj['attributes'][attribute]['objects']
                    if objects is not None:
                        node1 = obj_type.replace('SAI_OBJECT_TYPE_', '')
                        node2 = obj['attributes'][attribute]['objects'][0].replace(
                            'SAI_OBJECT_TYPE_', ''
                        )
                        if node1 == node2:
                            node2 = obj['attributes'][attribute]['objects'][1].replace(
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
    generate_pyetes_test(
        obj_type,
    )
