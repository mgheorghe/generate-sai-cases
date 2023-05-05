from pprint import pprint

import pytest


class TestSaiBfdSession:
    # object with parent SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SRV6_SIDLIST

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
                    '1',
                    'SAI_BFD_SESSION_ATTR_SRC_IP_ADDRESS',
                    '180.0.0.1',
                    'SAI_BFD_SESSION_ATTR_DST_IP_ADDRESS',
                    '180.0.0.1',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_SRC_IP_ADDRESS',
                    '180.0.0.1',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_DST_IP_ADDRESS',
                    '180.0.0.1',
                    'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_MIN_TX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MIN_RX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MULTIPLIER',
                    '1',
                    'SAI_BFD_SESSION_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_virtual_router_set')
    def test_sai_bfd_session_attr_virtual_router_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_virtual_router_set'])
    def test_sai_bfd_session_attr_virtual_router_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_port_set')
    def test_sai_bfd_session_attr_port_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_PORT', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_port_set'])
    def test_sai_bfd_session_attr_port_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_tc_set')
    def test_sai_bfd_session_attr_tc_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_TC', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_tc_set'])
    def test_sai_bfd_session_attr_tc_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_TC'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_vlan_tpid_set')
    def test_sai_bfd_session_attr_vlan_tpid_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_VLAN_TPID', '0x8100'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_vlan_tpid_set'])
    def test_sai_bfd_session_attr_vlan_tpid_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_VLAN_TPID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0x8100', 'Get error, expected 0x8100 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_vlan_pri_set')
    def test_sai_bfd_session_attr_vlan_pri_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_VLAN_PRI', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_vlan_pri_set'])
    def test_sai_bfd_session_attr_vlan_pri_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_VLAN_PRI'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_vlan_cfi_set')
    def test_sai_bfd_session_attr_vlan_cfi_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_VLAN_CFI', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_vlan_cfi_set'])
    def test_sai_bfd_session_attr_vlan_cfi_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_VLAN_CFI'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_iphdr_version_set')
    def test_sai_bfd_session_attr_iphdr_version_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_IPHDR_VERSION', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_iphdr_version_set'])
    def test_sai_bfd_session_attr_iphdr_version_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_IPHDR_VERSION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_tos_set')
    def test_sai_bfd_session_attr_tos_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_TOS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_tos_set'])
    def test_sai_bfd_session_attr_tos_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_TOS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_ttl_set')
    def test_sai_bfd_session_attr_ttl_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_TTL', '255'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_ttl_set'])
    def test_sai_bfd_session_attr_ttl_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_TTL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '255', 'Get error, expected 255 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_tunnel_tos_set')
    def test_sai_bfd_session_attr_tunnel_tos_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_TUNNEL_TOS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_tunnel_tos_set'])
    def test_sai_bfd_session_attr_tunnel_tos_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_TUNNEL_TOS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_tunnel_ttl_set')
    def test_sai_bfd_session_attr_tunnel_ttl_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_TUNNEL_TTL', '255'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_tunnel_ttl_set'])
    def test_sai_bfd_session_attr_tunnel_ttl_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_TUNNEL_TTL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '255', 'Get error, expected 255 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_src_mac_address_set')
    def test_sai_bfd_session_attr_src_mac_address_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_src_mac_address_set'])
    def test_sai_bfd_session_attr_src_mac_address_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_dst_mac_address_set')
    def test_sai_bfd_session_attr_dst_mac_address_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_dst_mac_address_set'])
    def test_sai_bfd_session_attr_dst_mac_address_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_echo_enable_set')
    def test_sai_bfd_session_attr_echo_enable_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_ECHO_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_echo_enable_set'])
    def test_sai_bfd_session_attr_echo_enable_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_ECHO_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_min_tx_set')
    def test_sai_bfd_session_attr_min_tx_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_MIN_TX', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_min_tx_set'])
    def test_sai_bfd_session_attr_min_tx_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_MIN_TX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_min_rx_set')
    def test_sai_bfd_session_attr_min_rx_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_MIN_RX', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_min_rx_set'])
    def test_sai_bfd_session_attr_min_rx_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_MIN_RX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bfd_session_attr_multiplier_set')
    def test_sai_bfd_session_attr_multiplier_set(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'set',
                'attributes': ['SAI_BFD_SESSION_ATTR_MULTIPLIER', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bfd_session_attr_multiplier_set'])
    def test_sai_bfd_session_attr_multiplier_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_MULTIPLIER'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_remote_min_tx_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_REMOTE_MIN_TX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_remote_min_rx_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_REMOTE_MIN_RX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_state_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_STATE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_negotiated_tx_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_NEGOTIATED_TX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_negotiated_rx_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_NEGOTIATED_RX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_local_diag_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_LOCAL_DIAG'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_remote_diag_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_REMOTE_DIAG'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_bfd_session_attr_remote_multiplier_get(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'get',
                'attributes': ['SAI_BFD_SESSION_ATTR_REMOTE_MULTIPLIER'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_bfd_session_remove(self, npu):
        commands = [
            {'name': 'bfd_session_1', 'op': 'remove'},
            {'name': 'srv6_sidlist_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
            {'name': 'virtual_router_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
