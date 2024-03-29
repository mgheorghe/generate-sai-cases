from pprint import pprint

import pytest


@pytest.mark.npu
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

    @pytest.mark.dependency(
        name='test_sai_switch_tunnel_attr_loopback_packet_action_set'
    )
    def test_sai_switch_tunnel_attr_loopback_packet_action_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_LOOPBACK_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_switch_tunnel_attr_loopback_packet_action_set']
    )
    def test_sai_switch_tunnel_attr_loopback_packet_action_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_LOOPBACK_PACKET_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PACKET_ACTION_FORWARD', (
            'Get error, expected SAI_PACKET_ACTION_FORWARD but got %s' % r_value
        )

    @pytest.mark.dependency(
        name='test_sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_set'
    )
    def test_sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_TUNNEL_VXLAN_UDP_SPORT_MODE',
                    'SAI_TUNNEL_VXLAN_UDP_SPORT_MODE_EPHEMERAL',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_set']
    )
    def test_sai_switch_tunnel_attr_tunnel_vxlan_udp_sport_mode_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_TUNNEL_VXLAN_UDP_SPORT_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_TUNNEL_VXLAN_UDP_SPORT_MODE_EPHEMERAL', (
            'Get error, expected SAI_TUNNEL_VXLAN_UDP_SPORT_MODE_EPHEMERAL but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_switch_tunnel_attr_vxlan_udp_sport_set')
    def test_sai_switch_tunnel_attr_vxlan_udp_sport_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_switch_tunnel_attr_vxlan_udp_sport_set'])
    def test_sai_switch_tunnel_attr_vxlan_udp_sport_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_switch_tunnel_attr_vxlan_udp_sport_mask_set')
    def test_sai_switch_tunnel_attr_vxlan_udp_sport_mask_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT_MASK', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_switch_tunnel_attr_vxlan_udp_sport_mask_set']
    )
    def test_sai_switch_tunnel_attr_vxlan_udp_sport_mask_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_VXLAN_UDP_SPORT_MASK'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_set'
    )
    def test_sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_AND_COLOR_TO_DSCP_MAP',
                    'null',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_set']
    )
    def test_sai_switch_tunnel_attr_encap_qos_tc_and_color_to_dscp_map_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_AND_COLOR_TO_DSCP_MAP'
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_set'
    )
    def test_sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_TO_QUEUE_MAP',
                    'null',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_set']
    )
    def test_sai_switch_tunnel_attr_encap_qos_tc_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_ENCAP_QOS_TC_TO_QUEUE_MAP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_set'
    )
    def test_sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_DSCP_TO_TC_MAP',
                    'null',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_set']
    )
    def test_sai_switch_tunnel_attr_decap_qos_dscp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': ['SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_DSCP_TO_TC_MAP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_set'
    )
    def test_sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_set(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'set',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_TC_TO_PRIORITY_GROUP_MAP',
                    'null',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_set']
    )
    def test_sai_switch_tunnel_attr_decap_qos_tc_to_priority_group_map_get(self, npu):
        commands = [
            {
                'name': 'switch_tunnel_1',
                'op': 'get',
                'attributes': [
                    'SAI_SWITCH_TUNNEL_ATTR_DECAP_QOS_TC_TO_PRIORITY_GROUP_MAP'
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    def test_switch_tunnel_remove(self, npu):
        commands = [{'name': 'switch_tunnel_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
