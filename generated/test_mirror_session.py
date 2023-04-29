from pprint import pprint

import pytest


class TestSaiMirrorSession:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT

    @pytest.mark.dependency(scope='session')
    def test_mirror_session_create(self, npu):
        commands = [
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
                'name': 'mirror_session_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'attributes': [
                    'SAI_MIRROR_SESSION_ATTR_TYPE',
                    'SAI_MIRROR_SESSION_TYPE_LOCAL',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORT',
                    '$port_1',
                    'SAI_MIRROR_SESSION_ATTR_ERSPAN_ENCAPSULATION_TYPE',
                    'SAI_ERSPAN_ENCAPSULATION_TYPE_MIRROR_L3_GRE_TUNNEL',
                    'SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_TOS',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST',
                    'sai_object_list_t',
                    'SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_mirror_session_attr_monitor_port_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_monitor_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_MONITOR_PORT', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_monitor_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_monitor_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_MONITOR_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_truncate_size_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_truncate_size_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TRUNCATE_SIZE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_truncate_size_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_truncate_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_TRUNCATE_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_sample_rate_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_sample_rate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_SAMPLE_RATE', '1'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_sample_rate_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_sample_rate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_SAMPLE_RATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_congestion_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_congestion_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': [
                    'SAI_MIRROR_SESSION_ATTR_CONGESTION_MODE',
                    'SAI_MIRROR_SESSION_CONGESTION_MODE_INDEPENDENT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_congestion_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_congestion_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_CONGESTION_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_MIRROR_SESSION_CONGESTION_MODE_INDEPENDENT'
                for result in results
            ]
        ), 'Get error'

    def test_sai_mirror_session_attr_tc_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TC', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_tc_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_tpid_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_TPID', '0x8100'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_tpid_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_VLAN_TPID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x8100' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_ID', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_pri_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_pri_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_PRI', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_pri_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_pri_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_VLAN_PRI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_cfi_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_cfi_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_CFI', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_cfi_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_cfi_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_VLAN_CFI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_header_valid_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_header_valid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_HEADER_VALID', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_vlan_header_valid_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_vlan_header_valid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_VLAN_HEADER_VALID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_iphdr_version_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_iphdr_version_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_iphdr_version_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_iphdr_version_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_tos_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_tos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TOS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_tos_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_tos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_TOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_ttl_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TTL', '255'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_ttl_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '255' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_src_ip_address_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_src_ip_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_src_ip_address_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_src_ip_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_dst_ip_address_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_dst_ip_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_dst_ip_address_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_dst_ip_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_src_mac_address_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_src_mac_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_src_mac_address_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_src_mac_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_dst_mac_address_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_dst_mac_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_dst_mac_address_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_dst_mac_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_gre_protocol_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_gre_protocol_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_gre_protocol_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_gre_protocol_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_monitor_portlist_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_monitor_portlist_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_monitor_portlist_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_monitor_portlist_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_policer_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_policer_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_POLICER', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_policer_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_policer_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_POLICER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_udp_src_port_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_udp_src_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_udp_src_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_udp_src_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_udp_dst_port_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_udp_dst_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_udp_dst_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_udp_dst_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': [
                    'SAI_MIRROR_SESSION_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mirror_session_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_mirror_session_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': 'SAI_MIRROR_SESSION_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_mirror_session_remove(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'attributes': [
                    'SAI_MIRROR_SESSION_ATTR_TYPE',
                    'SAI_MIRROR_SESSION_TYPE_LOCAL',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORT',
                    '$port_1',
                    'SAI_MIRROR_SESSION_ATTR_ERSPAN_ENCAPSULATION_TYPE',
                    'SAI_ERSPAN_ENCAPSULATION_TYPE_MIRROR_L3_GRE_TUNNEL',
                    'SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_TOS',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST',
                    'sai_object_list_t',
                    'SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT',
                    '10',
                ],
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
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
