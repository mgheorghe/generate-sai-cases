from pprint import pprint

import pytest


class TestSaiFdbEntry:
    # object with no parents

    def test_fdb_entry_create(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'SAI_FDB_ENTRY_TYPE_DYNAMIC'],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_type_set')
    def test_sai_fdb_entry_attr_type_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_type_set'])
    def test_sai_fdb_entry_attr_type_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_packet_action_set')
    def test_sai_fdb_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_FDB_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_packet_action_set'])
    def test_sai_fdb_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_PACKET_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PACKET_ACTION_FORWARD', (
            'Get error, expected SAI_PACKET_ACTION_FORWARD but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_user_trap_id_set')
    def test_sai_fdb_entry_attr_user_trap_id_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': ['SAI_FDB_ENTRY_ATTR_USER_TRAP_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_user_trap_id_set'])
    def test_sai_fdb_entry_attr_user_trap_id_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_USER_TRAP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_bridge_port_id_set')
    def test_sai_fdb_entry_attr_bridge_port_id_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_FDB_ENTRY_ATTR_BRIDGE_PORT_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_bridge_port_id_set'])
    def test_sai_fdb_entry_attr_bridge_port_id_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_BRIDGE_PORT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_meta_data_set')
    def test_sai_fdb_entry_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': ['SAI_FDB_ENTRY_ATTR_META_DATA', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_meta_data_set'])
    def test_sai_fdb_entry_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_META_DATA'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_endpoint_ip_set')
    def test_sai_fdb_entry_attr_endpoint_ip_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': ['SAI_FDB_ENTRY_ATTR_ENDPOINT_IP', '0.0.0.0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_endpoint_ip_set'])
    def test_sai_fdb_entry_attr_endpoint_ip_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_ENDPOINT_IP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_counter_id_set')
    def test_sai_fdb_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': ['SAI_FDB_ENTRY_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_counter_id_set'])
    def test_sai_fdb_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_COUNTER_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_fdb_entry_attr_allow_mac_move_set')
    def test_sai_fdb_entry_attr_allow_mac_move_set(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'set',
                'attributes': ['SAI_FDB_ENTRY_ATTR_ALLOW_MAC_MOVE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_fdb_entry_attr_allow_mac_move_set'])
    def test_sai_fdb_entry_attr_allow_mac_move_get(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'get',
                'attributes': ['SAI_FDB_ENTRY_ATTR_ALLOW_MAC_MOVE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    def test_fdb_entry_remove(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
