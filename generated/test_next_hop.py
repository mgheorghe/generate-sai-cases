from pprint import pprint

import pytest


class TestSaiNextHop:
    # object with parent SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_TUNNEL SAI_OBJECT_TYPE_SRV6_SIDLIST

    def test_next_hop_create(self, npu):
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
                'name': 'srv6_sidlist_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            },
            {
                'name': 'next_hop_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'attributes': [
                    'SAI_NEXT_HOP_ATTR_TYPE',
                    'SAI_NEXT_HOP_TYPE_IP',
                    'SAI_NEXT_HOP_ATTR_IP',
                    'sai_ip_address_t',
                    'SAI_NEXT_HOP_ATTR_ROUTER_INTERFACE_ID',
                    '$router_interface_1',
                    'SAI_NEXT_HOP_ATTR_TUNNEL_ID',
                    '$tunnel_1',
                    'SAI_NEXT_HOP_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                    'SAI_NEXT_HOP_ATTR_LABELSTACK',
                    '2:10,11',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_next_hop_attr_tunnel_vni_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_tunnel_vni_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': ['SAI_NEXT_HOP_ATTR_TUNNEL_VNI', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_tunnel_vni_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_tunnel_vni_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_TUNNEL_VNI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_next_hop_attr_tunnel_mac_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_tunnel_mac_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': [
                    'SAI_NEXT_HOP_ATTR_TUNNEL_MAC',
                    'attrvalue SAI_SWITCH_ATTR_VXLAN_DEFAULT_ROUTER_MAC',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_tunnel_mac_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_tunnel_mac_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_TUNNEL_MAC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'attrvalue SAI_SWITCH_ATTR_VXLAN_DEFAULT_ROUTER_MAC'
                for result in results
            ]
        ), 'Get error'

    def test_sai_next_hop_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': ['SAI_NEXT_HOP_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_next_hop_attr_disable_decrement_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_disable_decrement_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': ['SAI_NEXT_HOP_ATTR_DISABLE_DECREMENT_TTL', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_disable_decrement_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_disable_decrement_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_DISABLE_DECREMENT_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_next_hop_attr_outseg_type_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': ['SAI_NEXT_HOP_ATTR_OUTSEG_TYPE', 'SAI_OUTSEG_TYPE_SWAP'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_outseg_type_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_OUTSEG_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_OUTSEG_TYPE_SWAP' for result in results]
        ), 'Get error'

    def test_sai_next_hop_attr_outseg_ttl_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_ttl_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': [
                    'SAI_NEXT_HOP_ATTR_OUTSEG_TTL_MODE',
                    'SAI_OUTSEG_TTL_MODE_UNIFORM',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_outseg_ttl_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_ttl_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_OUTSEG_TTL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_OUTSEG_TTL_MODE_UNIFORM' for result in results]
        ), 'Get error'

    def test_sai_next_hop_attr_outseg_ttl_value_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_ttl_value_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': ['SAI_NEXT_HOP_ATTR_OUTSEG_TTL_VALUE', '255'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_outseg_ttl_value_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_ttl_value_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_OUTSEG_TTL_VALUE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '255' for result in results]), 'Get error'

    def test_sai_next_hop_attr_outseg_exp_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_exp_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': [
                    'SAI_NEXT_HOP_ATTR_OUTSEG_EXP_MODE',
                    'SAI_OUTSEG_EXP_MODE_UNIFORM',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_outseg_exp_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_exp_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_OUTSEG_EXP_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_OUTSEG_EXP_MODE_UNIFORM' for result in results]
        ), 'Get error'

    def test_sai_next_hop_attr_outseg_exp_value_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_exp_value_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': ['SAI_NEXT_HOP_ATTR_OUTSEG_EXP_VALUE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_outseg_exp_value_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_outseg_exp_value_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_OUTSEG_EXP_VALUE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_next_hop_attr_qos_tc_and_color_to_mpls_exp_map_set(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_qos_tc_and_color_to_mpls_exp_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': [
                    'SAI_NEXT_HOP_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_attr_qos_tc_and_color_to_mpls_exp_map_get(self, npu):
        commands = [
            {
                'name': 'sai_next_hop_attr_qos_tc_and_color_to_mpls_exp_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'atrribute': 'SAI_NEXT_HOP_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_next_hop_remove(self, npu):
        commands = [
            {
                'name': 'next_hop_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'attributes': [
                    'SAI_NEXT_HOP_ATTR_TYPE',
                    'SAI_NEXT_HOP_TYPE_IP',
                    'SAI_NEXT_HOP_ATTR_IP',
                    'sai_ip_address_t',
                    'SAI_NEXT_HOP_ATTR_ROUTER_INTERFACE_ID',
                    '$router_interface_1',
                    'SAI_NEXT_HOP_ATTR_TUNNEL_ID',
                    '$tunnel_1',
                    'SAI_NEXT_HOP_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                    'SAI_NEXT_HOP_ATTR_LABELSTACK',
                    '2:10,11',
                ],
            },
            {
                'name': 'srv6_sidlist_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            },
            {
                'name': 'tunnel_1',
                'op': 'remove',
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
                'name': 'router_interface_1',
                'op': 'remove',
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
                'name': 'bridge_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'vlan_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'virtual_router_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
