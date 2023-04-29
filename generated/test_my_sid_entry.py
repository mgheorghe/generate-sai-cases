from pprint import pprint

import pytest


class TestSaiMySidEntry:
    # object with no parents

    @pytest.mark.dependency(scope='session')
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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_my_sid_entry_attr_endpoint_behavior_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_endpoint_behavior_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_endpoint_behavior_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_endpoint_behavior_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_endpoint_behavior_flavor_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_endpoint_behavior_flavor_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': [
                    'SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR_FLAVOR',
                    'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_FLAVOR_NONE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_endpoint_behavior_flavor_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_endpoint_behavior_flavor_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR_FLAVOR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_FLAVOR_NONE'
                for result in results
            ]
        ), 'Get error'

    def test_sai_my_sid_entry_attr_packet_action_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': [
                    'SAI_MY_SID_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_packet_action_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_my_sid_entry_attr_trap_priority_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_trap_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': ['SAI_MY_SID_ENTRY_ATTR_TRAP_PRIORITY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_trap_priority_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_trap_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_TRAP_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_next_hop_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_next_hop_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': [
                    'SAI_MY_SID_ENTRY_ATTR_NEXT_HOP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_next_hop_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_next_hop_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_NEXT_HOP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_tunnel_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_tunnel_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': ['SAI_MY_SID_ENTRY_ATTR_TUNNEL_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_tunnel_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_tunnel_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_TUNNEL_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_vrf_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_vrf_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': ['SAI_MY_SID_ENTRY_ATTR_VRF', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_vrf_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_vrf_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_VRF',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': ['SAI_MY_SID_ENTRY_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_sid_entry_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_my_sid_entry_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'atrribute': 'SAI_MY_SID_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_my_sid_entry_remove(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'attributes': [
                    'SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR',
                    'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_E',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
