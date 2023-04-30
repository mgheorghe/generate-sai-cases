from pprint import pprint

import pytest


class TestSaiSchedulerGroup:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SCHEDULER_GROUP SAI_OBJECT_TYPE_PORT

    def test_scheduler_group_create(self, npu):
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
                'name': 'scheduler_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'attributes': [
                    'SAI_SCHEDULER_GROUP_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_SCHEDULER_GROUP_ATTR_LEVEL',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE',
                    'TODO_circular parent reference',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_scheduler_group_attr_child_count_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_group_attr_child_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'atrribute': 'SAI_SCHEDULER_GROUP_ATTR_CHILD_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_scheduler_group_attr_child_list_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_group_attr_child_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'atrribute': 'SAI_SCHEDULER_GROUP_ATTR_CHILD_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_scheduler_group_attr_scheduler_profile_id_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_group_attr_scheduler_profile_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'atrribute': [
                    'SAI_SCHEDULER_GROUP_ATTR_SCHEDULER_PROFILE_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_group_attr_scheduler_profile_id_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_group_attr_scheduler_profile_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'atrribute': 'SAI_SCHEDULER_GROUP_ATTR_SCHEDULER_PROFILE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_scheduler_group_attr_parent_node_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_group_attr_parent_node_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'atrribute': ['SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_group_attr_parent_node_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_group_attr_parent_node_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'atrribute': 'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_scheduler_group_remove(self, npu):
        commands = [
            {
                'name': 'scheduler_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'attributes': [
                    'SAI_SCHEDULER_GROUP_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_SCHEDULER_GROUP_ATTR_LEVEL',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE',
                    'TODO_circular parent reference',
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
