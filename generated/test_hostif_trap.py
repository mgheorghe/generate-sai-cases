from pprint import pprint

import pytest


class TestSaiHostifTrap:
    # object with no parents

    def test_hostif_trap_create(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'SAI_HOSTIF_TRAP_TYPE_STP',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_hostif_trap_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_trap_priority_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_trap_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_PRIORITY',
                    'attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_trap_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_trap_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_TRAP_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY'
                for result in results
            ]
        ), 'Get error'

    def test_sai_hostif_trap_attr_exclude_port_list_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_exclude_port_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_EXCLUDE_PORT_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_exclude_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_exclude_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_EXCLUDE_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_trap_group_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_trap_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_GROUP',
                    'attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_trap_group_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_trap_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_TRAP_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP'
                for result in results
            ]
        ), 'Get error'

    def test_sai_hostif_trap_attr_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_mirror_session_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_mirror_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_MIRROR_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_trap_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_trap_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_hostif_trap_remove(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'SAI_HOSTIF_TRAP_TYPE_STP',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
