from pprint import pprint

import pytest


class TestSaiInboundRoutingEntry:
    # object with no attributes

    def test_inbound_routing_entry_create(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_inbound_routing_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'sai_inbound_routing_entry_attr_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION',
                    'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inbound_routing_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'sai_inbound_routing_entry_attr_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP'
                for result in results
            ]
        ), 'Get error'

    def test_sai_inbound_routing_entry_attr_src_vnet_id_set(self, npu):
        commands = [
            {
                'name': 'sai_inbound_routing_entry_attr_src_vnet_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inbound_routing_entry_attr_src_vnet_id_get(self, npu):
        commands = [
            {
                'name': 'sai_inbound_routing_entry_attr_src_vnet_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_inbound_routing_entry_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'sai_inbound_routing_entry_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_INBOUND_ROUTING_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_inbound_routing_entry_remove(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
