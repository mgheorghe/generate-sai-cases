from pprint import pprint

import pytest


class TestSaiFdbEntry:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_fdb_entry_create(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'SAI_FDB_ENTRY_TYPE_DYNAMIC'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_fdb_entry_attr_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': ['SAI_FDB_ENTRY_ATTR_TYPE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_packet_action_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': [
                    'SAI_FDB_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_packet_action_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_fdb_entry_attr_user_trap_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_user_trap_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': ['SAI_FDB_ENTRY_ATTR_USER_TRAP_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_user_trap_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_user_trap_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_USER_TRAP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_bridge_port_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_bridge_port_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': [
                    'SAI_FDB_ENTRY_ATTR_BRIDGE_PORT_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_bridge_port_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_bridge_port_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_BRIDGE_PORT_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_meta_data_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_meta_data_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': ['SAI_FDB_ENTRY_ATTR_META_DATA', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_meta_data_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_meta_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_META_DATA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_endpoint_ip_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_endpoint_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': ['SAI_FDB_ENTRY_ATTR_ENDPOINT_IP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_endpoint_ip_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_endpoint_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_ENDPOINT_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': ['SAI_FDB_ENTRY_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_allow_mac_move_set(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_allow_mac_move_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': ['SAI_FDB_ENTRY_ATTR_ALLOW_MAC_MOVE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_fdb_entry_attr_allow_mac_move_get(self, dpu):
        commands = [
            {
                'name': 'sai_fdb_entry_attr_allow_mac_move_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'atrribute': 'SAI_FDB_ENTRY_ATTR_ALLOW_MAC_MOVE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_fdb_entry_remove(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'SAI_FDB_ENTRY_TYPE_DYNAMIC'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
