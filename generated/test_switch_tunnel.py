from pprint import pprint

import pytest


class TestSaiSwitchTunnel:
    # object with no parents

    def test_switch_tunnel_create(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_TUNNEL_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_switch_tunnel_attr_loopback_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_loopback_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': [
                    'SAI_SWITCH_TUNNEL_ATTR_LOOPBACK_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_loopback_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_loopback_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_LOOPBACK_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': [
                    'SAI_SWITCH_TUNNEL_ATTR_TUNNEL_VXLAN_UDP_SPORT_MODE',
                    'SAI_TUNNEL_VXLAN_UDP_SPORT_MODE_EPHEMERAL',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_TUNNEL_VXLAN_UDP_SPORT_MODE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_TUNNEL_VXLAN_UDP_SPORT_MODE_EPHEMERAL'
                for result in results
            ]
        ), 'Get error'

    def test_sai_switch_tunnel_attr_vxlan_udp_sport_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_vxlan_udp_sport_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': ['SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_vxlan_udp_sport_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_vxlan_udp_sport_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_vxlan_udp_sport_mask_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_vxlan_udp_sport_mask_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': ['SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT_MASK', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_vxlan_udp_sport_mask_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_vxlan_udp_sport_mask_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT_MASK',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': [
                    'SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_AND_COLOR_TO_DSCP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_AND_COLOR_TO_DSCP_MAP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': [
                    'SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_TO_QUEUE_MAP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': [
                    'SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_DSCP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_DSCP_TO_TC_MAP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': [
                    'SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_TC_TO_PRIORITY_GROUP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'atrribute': 'SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_TC_TO_PRIORITY_GROUP_MAP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_switch_tunnel_remove(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_TUNNEL_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
