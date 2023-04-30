from pprint import pprint

import pytest


class TestSaiNeighborEntry:
    # object with no parents

    def test_neighbor_entry_create(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'attributes': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_neighbor_entry_attr_dst_mac_address_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_dst_mac_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_dst_mac_address_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_dst_mac_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_neighbor_entry_attr_user_trap_id_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_user_trap_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_USER_TRAP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_user_trap_id_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_user_trap_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_USER_TRAP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_no_host_route_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_no_host_route_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_NO_HOST_ROUTE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_no_host_route_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_no_host_route_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_NO_HOST_ROUTE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_meta_data_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_META_DATA', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_meta_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_META_DATA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_encap_index_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_encap_index_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_INDEX', 'internal'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_encap_index_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_encap_index_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_INDEX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_encap_impose_index_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_encap_impose_index_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_IMPOSE_INDEX', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_encap_impose_index_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_encap_impose_index_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_IMPOSE_INDEX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_is_local_set(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_is_local_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_IS_LOCAL', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_is_local_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_is_local_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_IS_LOCAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_neighbor_entry_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'sai_neighbor_entry_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_neighbor_entry_remove(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'attributes': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
