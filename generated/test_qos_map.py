from pprint import pprint

import pytest


class TestSaiQosMap:
    # object with no parents

    @pytest.mark.dependency(scope='session')
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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
