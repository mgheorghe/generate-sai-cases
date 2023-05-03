from pprint import pprint

import pytest


class TestSaiQosMap:
    # object with no parents

    def test_qos_map_create(self, npu):
        commands = [
            {
                'name': 'qos_map_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_QOS_MAP',
                'attributes': [
                    'SAI_QOS_MAP_ATTR_TYPE',
                    'SAI_QOS_MAP_TYPE_DOT1P_TO_TC',
                    'SAI_QOS_MAP_ATTR_MAP_TO_VALUE_LIST',
                    '2:10,11',
                ],
                'key': {'key': 'TODO', 'value': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_qos_map_attr_map_to_value_list_set(self, npu):
        commands = [
            {
                'name': 'qos_map_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QOS_MAP',
                'atrribute': ['SAI_QOS_MAP_ATTR_MAP_TO_VALUE_LIST', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_qos_map_attr_map_to_value_list_set'])
    def test_sai_qos_map_attr_map_to_value_list_get(self, npu):
        commands = [
            {
                'name': 'qos_map_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QOS_MAP',
                'atrribute': 'SAI_QOS_MAP_ATTR_MAP_TO_VALUE_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_qos_map_remove(self, npu):
        commands = [
            {
                'name': 'qos_map_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_QOS_MAP',
                'attributes': [
                    'SAI_QOS_MAP_ATTR_TYPE',
                    'SAI_QOS_MAP_TYPE_DOT1P_TO_TC',
                    'SAI_QOS_MAP_ATTR_MAP_TO_VALUE_LIST',
                    '2:10,11',
                ],
                'key': {'key': 'TODO', 'value': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
