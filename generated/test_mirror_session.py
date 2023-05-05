from pprint import pprint

import pytest


class TestSaiMirrorSession:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT

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
                    '1',
                    'SAI_MIRROR_SESSION_ATTR_TOS',
                    '1',
                    'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS',
                    '180.0.0.1',
                    'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS',
                    '180.0.0.1',
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

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_monitor_port_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_MONITOR_PORT', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_monitor_port_set'])
    def test_sai_mirror_session_attr_monitor_port_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_MONITOR_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_truncate_size_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TRUNCATE_SIZE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_truncate_size_set'])
    def test_sai_mirror_session_attr_truncate_size_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_TRUNCATE_SIZE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_sample_rate_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_SAMPLE_RATE', '1'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_sample_rate_set'])
    def test_sai_mirror_session_attr_sample_rate_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_SAMPLE_RATE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '1', (
            'Get error, expected 1 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_congestion_mode_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': [
                    'SAI_MIRROR_SESSION_ATTR_CONGESTION_MODE',
                    'SAI_MIRROR_SESSION_CONGESTION_MODE_INDEPENDENT',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_mirror_session_attr_congestion_mode_set']
    )
    def test_sai_mirror_session_attr_congestion_mode_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_CONGESTION_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[0][0].value() == 'SAI_MIRROR_SESSION_CONGESTION_MODE_INDEPENDENT'
        ), (
            'Get error, expected SAI_MIRROR_SESSION_CONGESTION_MODE_INDEPENDENT but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_tc_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TC', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_tc_set'])
    def test_sai_mirror_session_attr_tc_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_TC'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_vlan_tpid_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_TPID', '0x8100'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_vlan_tpid_set'])
    def test_sai_mirror_session_attr_vlan_tpid_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_VLAN_TPID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0x8100', (
            'Get error, expected 0x8100 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_ID', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_vlan_id_set'])
    def test_sai_mirror_session_attr_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_VLAN_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_vlan_pri_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_PRI', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_vlan_pri_set'])
    def test_sai_mirror_session_attr_vlan_pri_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_VLAN_PRI'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_vlan_cfi_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_CFI', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_vlan_cfi_set'])
    def test_sai_mirror_session_attr_vlan_cfi_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_VLAN_CFI'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_vlan_header_valid_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_VLAN_HEADER_VALID', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_mirror_session_attr_vlan_header_valid_set']
    )
    def test_sai_mirror_session_attr_vlan_header_valid_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_VLAN_HEADER_VALID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_iphdr_version_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_iphdr_version_set'])
    def test_sai_mirror_session_attr_iphdr_version_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_tos_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TOS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_tos_set'])
    def test_sai_mirror_session_attr_tos_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_TOS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_ttl_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_TTL', '255'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_ttl_set'])
    def test_sai_mirror_session_attr_ttl_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_TTL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '255', (
            'Get error, expected 255 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_src_ip_address_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_src_ip_address_set'])
    def test_sai_mirror_session_attr_src_ip_address_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_dst_ip_address_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_dst_ip_address_set'])
    def test_sai_mirror_session_attr_dst_ip_address_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_src_mac_address_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_mirror_session_attr_src_mac_address_set']
    )
    def test_sai_mirror_session_attr_src_mac_address_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_dst_mac_address_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_mirror_session_attr_dst_mac_address_set']
    )
    def test_sai_mirror_session_attr_dst_mac_address_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_gre_protocol_type_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_mirror_session_attr_gre_protocol_type_set']
    )
    def test_sai_mirror_session_attr_gre_protocol_type_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_monitor_portlist_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_mirror_session_attr_monitor_portlist_set']
    )
    def test_sai_mirror_session_attr_monitor_portlist_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_policer_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_POLICER', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_policer_set'])
    def test_sai_mirror_session_attr_policer_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_POLICER'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_udp_src_port_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_udp_src_port_set'])
    def test_sai_mirror_session_attr_udp_src_port_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_udp_dst_port_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': ['SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_udp_dst_port_set'])
    def test_sai_mirror_session_attr_udp_dst_port_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mirror_session_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'atrribute': [
                    'SAI_MIRROR_SESSION_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mirror_session_attr_counter_id_set'])
    def test_sai_mirror_session_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'get',
                'attributes': ['SAI_MIRROR_SESSION_ATTR_COUNTER_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_mirror_session_remove(self, npu):
        commands = [
            {'name': 'mirror_session_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
