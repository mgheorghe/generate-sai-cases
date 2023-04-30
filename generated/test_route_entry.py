from pprint import pprint

import pytest


class TestSaiRouteEntry:
    # object with no attributes

    def test_route_entry_create(self, npu):
        commands = [
            {
                'name': 'route_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_route_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': [
                    'SAI_ROUTE_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_route_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': 'SAI_ROUTE_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_route_entry_attr_user_trap_id_set(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_user_trap_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': [
                    'SAI_ROUTE_ENTRY_ATTR_USER_TRAP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_route_entry_attr_user_trap_id_get(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_user_trap_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': 'SAI_ROUTE_ENTRY_ATTR_USER_TRAP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_route_entry_attr_next_hop_id_set(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_next_hop_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': ['SAI_ROUTE_ENTRY_ATTR_NEXT_HOP_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_route_entry_attr_next_hop_id_get(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_next_hop_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': 'SAI_ROUTE_ENTRY_ATTR_NEXT_HOP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_route_entry_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_meta_data_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': ['SAI_ROUTE_ENTRY_ATTR_META_DATA', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_route_entry_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_meta_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': 'SAI_ROUTE_ENTRY_ATTR_META_DATA',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_route_entry_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': 'SAI_ROUTE_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_route_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': ['SAI_ROUTE_ENTRY_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_route_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': 'SAI_ROUTE_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_route_entry_attr_prefix_agg_id_set(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_prefix_agg_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': ['SAI_ROUTE_ENTRY_ATTR_PREFIX_AGG_ID', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_route_entry_attr_prefix_agg_id_get(self, npu):
        commands = [
            {
                'name': 'sai_route_entry_attr_prefix_agg_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'atrribute': 'SAI_ROUTE_ENTRY_ATTR_PREFIX_AGG_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_route_entry_remove(self, npu):
        commands = [
            {
                'name': 'route_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
