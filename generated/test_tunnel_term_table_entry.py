from pprint import pprint

import pytest


class TestSaiTunnelTermTableEntry:
    # object with parent SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_TUNNEL

    def test_tunnel_term_table_entry_create(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'vlan_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            },
            {
                'name': 'bridge_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'router_interface_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'attributes': [
                    'SAI_ROUTER_INTERFACE_ATTR_VIRTUAL_ROUTER_ID',
                    '$virtual_router_1',
                    'SAI_ROUTER_INTERFACE_ATTR_TYPE',
                    'SAI_ROUTER_INTERFACE_TYPE_PORT',
                    'SAI_ROUTER_INTERFACE_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_ROUTER_INTERFACE_ATTR_VLAN_ID',
                    '$vlan_1',
                    'SAI_ROUTER_INTERFACE_ATTR_OUTER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_INNER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'tunnel_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'attributes': [
                    'SAI_TUNNEL_ATTR_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE',
                    '$router_interface_1',
                    'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE',
                    '$router_interface_1',
                ],
            },
            {
                'name': 'tunnel_term_table_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_TERM_TABLE_ENTRY',
                'attributes': [
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_VR_ID',
                    '$virtual_router_1',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_TYPE',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_TYPE_P2P',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_DST_IP',
                    '180.0.0.1',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_SRC_IP',
                    '180.0.0.1',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_TUNNEL_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_ACTION_TUNNEL_ID',
                    '$tunnel_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tunnel_term_table_entry_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'tunnel_term_table_entry_1',
                'op': 'get',
                'attributes': ['SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_IP_ADDR_FAMILY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_tunnel_term_table_entry_attr_ipsec_verified_set'
    )
    def test_sai_tunnel_term_table_entry_attr_ipsec_verified_set(self, npu):
        commands = [
            {
                'name': 'tunnel_term_table_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_IPSEC_VERIFIED',
                    'true',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tunnel_term_table_entry_attr_ipsec_verified_set']
    )
    def test_sai_tunnel_term_table_entry_attr_ipsec_verified_get(self, npu):
        commands = [
            {
                'name': 'tunnel_term_table_entry_1',
                'op': 'get',
                'attributes': ['SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_IPSEC_VERIFIED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'true', 'Get error, expected true but got %s' % r_value

    def test_tunnel_term_table_entry_remove(self, npu):
        commands = [
            {'name': 'tunnel_term_table_entry_1', 'op': 'remove'},
            {'name': 'tunnel_1', 'op': 'remove'},
            {'name': 'router_interface_1', 'op': 'remove'},
            {'name': 'bridge_1', 'op': 'remove'},
            {'name': 'vlan_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
            {'name': 'virtual_router_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
