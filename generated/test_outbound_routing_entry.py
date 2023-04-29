from pprint import pprint

import pytest


class TestSaiOutboundRoutingEntry:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_outbound_routing_entry_create(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_outbound_routing_entry_attr_action_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION',
                    'SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_action_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET'
                for result in results
            ]
        ), 'Get error'

    def test_sai_outbound_routing_entry_attr_dst_vnet_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_dst_vnet_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_dst_vnet_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_dst_vnet_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_ip_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_IP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_ip_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_dip_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_dip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_dip_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_dip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_dip_mask_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_dip_mask_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP_MASK',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_dip_mask_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_dip_mask_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP_MASK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_sip_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_sip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_sip_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_sip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_sip_mask_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_sip_mask_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP_MASK',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_overlay_sip_mask_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_overlay_sip_mask_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP_MASK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_underlay_dip_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_underlay_dip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_DIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_underlay_dip_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_underlay_dip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_DIP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_underlay_sip_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_underlay_sip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_SIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_underlay_sip_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_underlay_sip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_SIP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_dash_encapsulation_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_dash_encapsulation_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DASH_ENCAPSULATION',
                    'SAI_DASH_ENCAPSULATION_VXLAN',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_dash_encapsulation_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_dash_encapsulation_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DASH_ENCAPSULATION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_DASH_ENCAPSULATION_VXLAN' for result in results]
        ), 'Get error'

    def test_sai_outbound_routing_entry_attr_tunnel_key_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_tunnel_key_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_TUNNEL_KEY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_tunnel_key_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_tunnel_key_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_TUNNEL_KEY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_outbound_routing_entry_attr_ip_addr_family_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_routing_entry_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_outbound_routing_entry_remove(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
