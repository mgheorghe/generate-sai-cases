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

    @pytest.mark.dependency()
    def test_sai_hostif_trap_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_trap_attr_packet_action_set'])
    def test_sai_hostif_trap_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_hostif_trap_attr_trap_priority_set(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_PRIORITY',
                    'attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_trap_attr_trap_priority_set'])
    def test_sai_hostif_trap_attr_trap_priority_get(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_TRAP_PRIORITY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[1][0].value()
            == 'attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY'
        ), (
            'Get error, expected attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_hostif_trap_attr_exclude_port_list_set(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_EXCLUDE_PORT_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_trap_attr_exclude_port_list_set'])
    def test_sai_hostif_trap_attr_exclude_port_list_get(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_EXCLUDE_PORT_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'empty', (
            'Get error, expected empty but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_hostif_trap_attr_trap_group_set(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_GROUP',
                    'attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_trap_attr_trap_group_set'])
    def test_sai_hostif_trap_attr_trap_group_get(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_TRAP_GROUP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[1][0].value() == 'attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP'
        ), (
            'Get error, expected attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_hostif_trap_attr_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_trap_attr_mirror_session_set'])
    def test_sai_hostif_trap_attr_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_MIRROR_SESSION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'empty', (
            'Get error, expected empty but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_hostif_trap_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': ['SAI_HOSTIF_TRAP_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_trap_attr_counter_id_set'])
    def test_sai_hostif_trap_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'atrribute': 'SAI_HOSTIF_TRAP_ATTR_COUNTER_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

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
