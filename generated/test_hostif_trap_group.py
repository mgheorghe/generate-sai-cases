from pprint import pprint

import pytest


class TestSaiHostifTrapGroup:
    # object with no attributes

    def test_hostif_trap_group_create(self, npu):
        commands = [
            {
                'name': 'hostif_trap_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_hostif_trap_group_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_group_attr_admin_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'atrribute': ['SAI_HOSTIF_TRAP_GROUP_ATTR_ADMIN_STATE', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_group_attr_admin_state_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_group_attr_admin_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'atrribute': 'SAI_HOSTIF_TRAP_GROUP_ATTR_ADMIN_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_hostif_trap_group_attr_queue_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_group_attr_queue_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'atrribute': ['SAI_HOSTIF_TRAP_GROUP_ATTR_QUEUE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_group_attr_queue_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_group_attr_queue_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'atrribute': 'SAI_HOSTIF_TRAP_GROUP_ATTR_QUEUE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_hostif_trap_group_attr_policer_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_group_attr_policer_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'atrribute': [
                    'SAI_HOSTIF_TRAP_GROUP_ATTR_POLICER',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_group_attr_policer_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_group_attr_policer_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'atrribute': 'SAI_HOSTIF_TRAP_GROUP_ATTR_POLICER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_hostif_trap_group_remove(self, npu):
        commands = [
            {
                'name': 'hostif_trap_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
