from pprint import pprint

import pytest


class TestSaiMySidEntry:
    # object with no parents

    def test_my_sid_entry_create(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'attributes': [
                    'SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR',
                    'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_E',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'locator_block_len': 'TODO',
                    'locator_node_len': 'TODO',
                    'function_len': 'TODO',
                    'args_len': 'TODO',
                    'sid': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_my_sid_entry_attr_endpoint_behavior_set')
    def test_sai_my_sid_entry_attr_endpoint_behavior_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_my_sid_entry_attr_endpoint_behavior_set']
    )
    def test_sai_my_sid_entry_attr_endpoint_behavior_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_my_sid_entry_attr_endpoint_behavior_flavor_set'
    )
    def test_sai_my_sid_entry_attr_endpoint_behavior_flavor_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR_FLAVOR',
                    'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_FLAVOR_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_my_sid_entry_attr_endpoint_behavior_flavor_set']
    )
    def test_sai_my_sid_entry_attr_endpoint_behavior_flavor_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR_FLAVOR'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_FLAVOR_NONE', (
            'Get error, expected SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_FLAVOR_NONE but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_my_sid_entry_attr_packet_action_set')
    def test_sai_my_sid_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_MY_SID_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_my_sid_entry_attr_packet_action_set'])
    def test_sai_my_sid_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_PACKET_ACTION'],
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

    @pytest.mark.dependency(name='test_sai_my_sid_entry_attr_trap_priority_set')
    def test_sai_my_sid_entry_attr_trap_priority_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_TRAP_PRIORITY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_my_sid_entry_attr_trap_priority_set'])
    def test_sai_my_sid_entry_attr_trap_priority_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_TRAP_PRIORITY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_my_sid_entry_attr_next_hop_id_set')
    def test_sai_my_sid_entry_attr_next_hop_id_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_MY_SID_ENTRY_ATTR_NEXT_HOP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_my_sid_entry_attr_next_hop_id_set'])
    def test_sai_my_sid_entry_attr_next_hop_id_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_NEXT_HOP_ID'],
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

    @pytest.mark.dependency(name='test_sai_my_sid_entry_attr_tunnel_id_set')
    def test_sai_my_sid_entry_attr_tunnel_id_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_TUNNEL_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_my_sid_entry_attr_tunnel_id_set'])
    def test_sai_my_sid_entry_attr_tunnel_id_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_TUNNEL_ID'],
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

    @pytest.mark.dependency(name='test_sai_my_sid_entry_attr_vrf_set')
    def test_sai_my_sid_entry_attr_vrf_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_VRF', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_my_sid_entry_attr_vrf_set'])
    def test_sai_my_sid_entry_attr_vrf_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_VRF'],
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

    @pytest.mark.dependency(name='test_sai_my_sid_entry_attr_counter_id_set')
    def test_sai_my_sid_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_MY_SID_ENTRY_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_my_sid_entry_attr_counter_id_set'])
    def test_sai_my_sid_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'get',
                'attributes': ['SAI_MY_SID_ENTRY_ATTR_COUNTER_ID'],
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

    def test_my_sid_entry_remove(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'locator_block_len': 'TODO',
                    'locator_node_len': 'TODO',
                    'function_len': 'TODO',
                    'args_len': 'TODO',
                    'sid': 'TODO',
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
