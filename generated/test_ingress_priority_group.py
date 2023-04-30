from pprint import pprint

import pytest


class TestSaiIngressPriorityGroup:
    # object with parent SAI_OBJECT_TYPE_PORT

    def test_ingress_priority_group_create(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'ingress_priority_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
                'attributes': [
                    'SAI_INGRESS_PRIORITY_GROUP_ATTR_PORT',
                    '$port_1',
                    'SAI_INGRESS_PRIORITY_GROUP_ATTR_INDEX',
                    'sai_uint8_t',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_ingress_priority_group_attr_buffer_profile_set(self, npu):
        commands = [
            {
                'name': 'sai_ingress_priority_group_attr_buffer_profile_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
                'atrribute': [
                    'SAI_INGRESS_PRIORITY_GROUP_ATTR_BUFFER_PROFILE',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ingress_priority_group_attr_buffer_profile_get(self, npu):
        commands = [
            {
                'name': 'sai_ingress_priority_group_attr_buffer_profile_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
                'atrribute': 'SAI_INGRESS_PRIORITY_GROUP_ATTR_BUFFER_PROFILE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_ingress_priority_group_attr_tam_set(self, npu):
        commands = [
            {
                'name': 'sai_ingress_priority_group_attr_tam_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
                'atrribute': ['SAI_INGRESS_PRIORITY_GROUP_ATTR_TAM', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ingress_priority_group_attr_tam_get(self, npu):
        commands = [
            {
                'name': 'sai_ingress_priority_group_attr_tam_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
                'atrribute': 'SAI_INGRESS_PRIORITY_GROUP_ATTR_TAM',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_ingress_priority_group_remove(self, npu):
        commands = [
            {
                'name': 'ingress_priority_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
                'attributes': [
                    'SAI_INGRESS_PRIORITY_GROUP_ATTR_PORT',
                    '$port_1',
                    'SAI_INGRESS_PRIORITY_GROUP_ATTR_INDEX',
                    'sai_uint8_t',
                ],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
