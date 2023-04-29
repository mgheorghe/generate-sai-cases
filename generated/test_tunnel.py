from pprint import pprint

import pytest


class TestSaiTunnel:
    # object with parent SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_ROUTER_INTERFACE

    @pytest.mark.dependency(scope='session')
    def test_tunnel_create(self, npu):
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
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tunnel_attr_encap_ttl_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_ttl_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_ENCAP_TTL_MODE',
                    'SAI_TUNNEL_TTL_MODE_UNIFORM_MODEL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_ttl_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_ttl_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_ENCAP_TTL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_TUNNEL_TTL_MODE_UNIFORM_MODEL' for result in results]
        ), 'Get error'

    def test_sai_tunnel_attr_encap_ttl_val_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_ttl_val_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_ENCAP_TTL_VAL', '255'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_ttl_val_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_ttl_val_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_ENCAP_TTL_VAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '255' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_dscp_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_dscp_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_ENCAP_DSCP_MODE',
                    'SAI_TUNNEL_DSCP_MODE_UNIFORM_MODEL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_dscp_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_dscp_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_ENCAP_DSCP_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_TUNNEL_DSCP_MODE_UNIFORM_MODEL' for result in results]
        ), 'Get error'

    def test_sai_tunnel_attr_encap_dscp_val_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_dscp_val_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_ENCAP_DSCP_VAL', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_dscp_val_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_dscp_val_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_ENCAP_DSCP_VAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_gre_key_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_gre_key_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_ENCAP_GRE_KEY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_gre_key_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_gre_key_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_ENCAP_GRE_KEY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tunnel_attr_decap_ttl_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_ttl_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_DECAP_TTL_MODE',
                    'SAI_TUNNEL_TTL_MODE_UNIFORM_MODEL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_decap_ttl_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_ttl_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_DECAP_TTL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_TUNNEL_TTL_MODE_UNIFORM_MODEL' for result in results]
        ), 'Get error'

    def test_sai_tunnel_attr_decap_dscp_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_dscp_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_DECAP_DSCP_MODE',
                    'SAI_TUNNEL_DSCP_MODE_UNIFORM_MODEL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_decap_dscp_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_dscp_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_DECAP_DSCP_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_TUNNEL_DSCP_MODE_UNIFORM_MODEL' for result in results]
        ), 'Get error'

    def test_sai_tunnel_attr_term_table_entry_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_term_table_entry_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_TERM_TABLE_ENTRY_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_tunnel_attr_loopback_packet_action_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_loopback_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_LOOPBACK_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_loopback_packet_action_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_loopback_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_LOOPBACK_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT_MODE',
                    'SAI_TUNNEL_VXLAN_UDP_SPORT_MODE_EPHEMERAL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_TUNNEL_VXLAN_UDP_SPORT_MODE_EPHEMERAL'
                for result in results
            ]
        ), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_mask_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_mask_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT_MASK', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_mask_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_mask_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT_MASK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tunnel_attr_sa_index_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_sa_index_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_SA_INDEX', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_sa_index_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_sa_index_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_SA_INDEX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tunnel_attr_ipsec_sa_port_list_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_ipsec_sa_port_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_IPSEC_SA_PORT_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_ipsec_sa_port_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_ipsec_sa_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_IPSEC_SA_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_ENCAP_QOS_TC_AND_COLOR_TO_DSCP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_ENCAP_QOS_TC_AND_COLOR_TO_DSCP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_qos_tc_to_queue_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_qos_tc_to_queue_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_ENCAP_QOS_TC_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_encap_qos_tc_to_queue_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_encap_qos_tc_to_queue_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_ENCAP_QOS_TC_TO_QUEUE_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_tunnel_attr_decap_qos_dscp_to_tc_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_qos_dscp_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_DECAP_QOS_DSCP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_decap_qos_dscp_to_tc_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_qos_dscp_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_DECAP_QOS_DSCP_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_tunnel_attr_decap_qos_tc_to_priority_group_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_qos_tc_to_priority_group_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': [
                    'SAI_TUNNEL_ATTR_DECAP_QOS_TC_TO_PRIORITY_GROUP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_decap_qos_tc_to_priority_group_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_decap_qos_tc_to_priority_group_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_DECAP_QOS_TC_TO_PRIORITY_GROUP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_security_set(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_security_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': ['SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT_SECURITY', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tunnel_attr_vxlan_udp_sport_security_get(self, dpu):
        commands = [
            {
                'name': 'sai_tunnel_attr_vxlan_udp_sport_security_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'atrribute': 'SAI_TUNNEL_ATTR_VXLAN_UDP_SPORT_SECURITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_tunnel_remove(self, npu):
        commands = [
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
