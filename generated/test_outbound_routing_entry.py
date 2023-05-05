from pprint import pprint

import pytest


class TestSaiOutboundRoutingEntry:
    # object with no attributes

    def test_outbound_routing_entry_create(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'attributes': [],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'eni_id': 'TODO',
                    'destination': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_outbound_routing_entry_attr_action_set')
    def test_sai_outbound_routing_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION',
                    'SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_outbound_routing_entry_attr_action_set'])
    def test_sai_outbound_routing_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET', (
            'Get error, expected SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_outbound_routing_entry_attr_dst_vnet_id_set')
    def test_sai_outbound_routing_entry_attr_dst_vnet_id_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_dst_vnet_id_set']
    )
    def test_sai_outbound_routing_entry_attr_dst_vnet_id_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID'],
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

    @pytest.mark.dependency(name='test_sai_outbound_routing_entry_attr_overlay_ip_set')
    def test_sai_outbound_routing_entry_attr_overlay_ip_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_IP', '0.0.0.0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_overlay_ip_set']
    )
    def test_sai_outbound_routing_entry_attr_overlay_ip_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_IP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_outbound_routing_entry_attr_overlay_dip_set')
    def test_sai_outbound_routing_entry_attr_overlay_dip_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_overlay_dip_set']
    )
    def test_sai_outbound_routing_entry_attr_overlay_dip_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_outbound_routing_entry_attr_overlay_dip_mask_set'
    )
    def test_sai_outbound_routing_entry_attr_overlay_dip_mask_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP_MASK',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_overlay_dip_mask_set']
    )
    def test_sai_outbound_routing_entry_attr_overlay_dip_mask_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP_MASK'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_outbound_routing_entry_attr_overlay_sip_set')
    def test_sai_outbound_routing_entry_attr_overlay_sip_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_overlay_sip_set']
    )
    def test_sai_outbound_routing_entry_attr_overlay_sip_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_outbound_routing_entry_attr_overlay_sip_mask_set'
    )
    def test_sai_outbound_routing_entry_attr_overlay_sip_mask_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP_MASK',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_overlay_sip_mask_set']
    )
    def test_sai_outbound_routing_entry_attr_overlay_sip_mask_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP_MASK'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_outbound_routing_entry_attr_underlay_dip_set'
    )
    def test_sai_outbound_routing_entry_attr_underlay_dip_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_DIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_underlay_dip_set']
    )
    def test_sai_outbound_routing_entry_attr_underlay_dip_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_DIP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_outbound_routing_entry_attr_underlay_sip_set'
    )
    def test_sai_outbound_routing_entry_attr_underlay_sip_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_SIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_underlay_sip_set']
    )
    def test_sai_outbound_routing_entry_attr_underlay_sip_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_SIP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_outbound_routing_entry_attr_dash_encapsulation_set'
    )
    def test_sai_outbound_routing_entry_attr_dash_encapsulation_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DASH_ENCAPSULATION',
                    'SAI_DASH_ENCAPSULATION_VXLAN',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_dash_encapsulation_set']
    )
    def test_sai_outbound_routing_entry_attr_dash_encapsulation_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DASH_ENCAPSULATION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_DASH_ENCAPSULATION_VXLAN', (
            'Get error, expected SAI_DASH_ENCAPSULATION_VXLAN but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_outbound_routing_entry_attr_tunnel_key_set')
    def test_sai_outbound_routing_entry_attr_tunnel_key_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_TUNNEL_KEY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_tunnel_key_set']
    )
    def test_sai_outbound_routing_entry_attr_tunnel_key_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_TUNNEL_KEY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_outbound_routing_entry_attr_counter_id_set')
    def test_sai_outbound_routing_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_ROUTING_ENTRY_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_routing_entry_attr_counter_id_set']
    )
    def test_sai_outbound_routing_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_ROUTING_ENTRY_ATTR_COUNTER_ID'],
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

    def test_outbound_routing_entry_remove(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'eni_id': 'TODO',
                    'destination': 'TODO',
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
