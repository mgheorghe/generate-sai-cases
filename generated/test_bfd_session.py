from pprint import pprint

import pytest


class TestSaiBfdSession:
    # object with parent SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SRV6_SIDLIST

    @pytest.mark.dependency(scope='session')
    def test_bfd_session_create(self, npu):
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
                'name': 'srv6_sidlist_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            },
            {
                'name': 'bfd_session_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'attributes': [
                    'SAI_BFD_SESSION_ATTR_TYPE',
                    'SAI_BFD_SESSION_TYPE_DEMAND_ACTIVE',
                    'SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER',
                    '$virtual_router_1',
                    'SAI_BFD_SESSION_ATTR_PORT',
                    '$port_1',
                    'SAI_BFD_SESSION_ATTR_LOCAL_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_REMOTE_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_BFD_SESSION_ATTR_VLAN_ID',
                    '10',
                    'SAI_BFD_SESSION_ATTR_BFD_ENCAPSULATION_TYPE',
                    'SAI_BFD_ENCAPSULATION_TYPE_IP_IN_IP',
                    'SAI_BFD_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_MIN_TX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MIN_RX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MULTIPLIER',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_bfd_session_attr_virtual_router_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_virtual_router_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_virtual_router_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_virtual_router_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_port_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_PORT', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tc_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_TC', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tc_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_vlan_tpid_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_vlan_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_VLAN_TPID', '0x8100'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_vlan_tpid_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_vlan_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_VLAN_TPID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x8100' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_vlan_pri_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_vlan_pri_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_VLAN_PRI', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_vlan_pri_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_vlan_pri_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_VLAN_PRI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_vlan_cfi_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_vlan_cfi_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_VLAN_CFI', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_vlan_cfi_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_vlan_cfi_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_VLAN_CFI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_iphdr_version_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_iphdr_version_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_IPHDR_VERSION', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_iphdr_version_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_iphdr_version_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_IPHDR_VERSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tos_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_TOS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tos_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_TOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_ttl_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_TTL', '255'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_ttl_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '255' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tunnel_tos_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tunnel_tos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_TUNNEL_TOS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tunnel_tos_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tunnel_tos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_TUNNEL_TOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tunnel_ttl_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tunnel_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_TUNNEL_TTL', '255'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_tunnel_ttl_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_tunnel_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_TUNNEL_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '255' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_src_mac_address_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_src_mac_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_src_mac_address_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_src_mac_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_dst_mac_address_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_dst_mac_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_dst_mac_address_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_dst_mac_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_echo_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_echo_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_ECHO_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_echo_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_echo_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_ECHO_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_min_tx_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_min_tx_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_MIN_TX', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_min_tx_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_min_tx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_MIN_TX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_min_rx_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_min_rx_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_MIN_RX', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_min_rx_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_min_rx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_MIN_RX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_multiplier_set(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_multiplier_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': ['SAI_BFD_SESSION_ATTR_MULTIPLIER', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_multiplier_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_multiplier_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_MULTIPLIER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_remote_min_tx_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_remote_min_tx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_REMOTE_MIN_TX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_remote_min_rx_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_remote_min_rx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_REMOTE_MIN_RX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_state_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_negotiated_tx_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_negotiated_tx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_NEGOTIATED_TX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_negotiated_rx_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_negotiated_rx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_NEGOTIATED_RX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_local_diag_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_local_diag_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_LOCAL_DIAG',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_remote_diag_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_remote_diag_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_REMOTE_DIAG',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bfd_session_attr_remote_multiplier_get(self, dpu):
        commands = [
            {
                'name': 'sai_bfd_session_attr_remote_multiplier_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'atrribute': 'SAI_BFD_SESSION_ATTR_REMOTE_MULTIPLIER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_bfd_session_remove(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'attributes': [
                    'SAI_BFD_SESSION_ATTR_TYPE',
                    'SAI_BFD_SESSION_TYPE_DEMAND_ACTIVE',
                    'SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER',
                    '$virtual_router_1',
                    'SAI_BFD_SESSION_ATTR_PORT',
                    '$port_1',
                    'SAI_BFD_SESSION_ATTR_LOCAL_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_REMOTE_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_BFD_SESSION_ATTR_VLAN_ID',
                    '10',
                    'SAI_BFD_SESSION_ATTR_BFD_ENCAPSULATION_TYPE',
                    'SAI_BFD_ENCAPSULATION_TYPE_IP_IN_IP',
                    'SAI_BFD_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_MIN_TX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MIN_RX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MULTIPLIER',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                ],
            },
            {
                'name': 'srv6_sidlist_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
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
