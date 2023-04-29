from pprint import pprint

import pytest


class TestSaiMacsec:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_macsec_create(self, npu):
        commands = [
            {
                'name': 'macsec_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'attributes': [
                    'SAI_MACSEC_ATTR_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_macsec_attr_switching_mode_cut_through_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_switching_mode_cut_through_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_SWITCHING_MODE_CUT_THROUGH_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_switching_mode_store_and_forward_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_switching_mode_store_and_forward_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_SWITCHING_MODE_STORE_AND_FORWARD_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_stats_mode_read_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_stats_mode_read_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_STATS_MODE_READ_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_stats_mode_read_clear_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_stats_mode_read_clear_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_STATS_MODE_READ_CLEAR_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_sci_in_ingress_macsec_acl_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_sci_in_ingress_macsec_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_SCI_IN_INGRESS_MACSEC_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_supported_cipher_suite_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_supported_cipher_suite_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_SUPPORTED_CIPHER_SUITE_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_pn_32bit_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_pn_32bit_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_PN_32BIT_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_xpn_64bit_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_xpn_64bit_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_XPN_64BIT_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_gcm_aes128_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_gcm_aes128_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_GCM_AES128_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_gcm_aes256_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_gcm_aes256_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_GCM_AES256_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_sectag_offsets_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_sectag_offsets_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_SECTAG_OFFSETS_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_system_side_mtu_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_system_side_mtu_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_SYSTEM_SIDE_MTU',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_warm_boot_supported_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_warm_boot_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_WARM_BOOT_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_warm_boot_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_warm_boot_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': ['SAI_MACSEC_ATTR_WARM_BOOT_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_attr_warm_boot_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_warm_boot_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_WARM_BOOT_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_macsec_attr_ctag_tpid_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_ctag_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': ['SAI_MACSEC_ATTR_CTAG_TPID', '0x8100'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_attr_ctag_tpid_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_ctag_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_CTAG_TPID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x8100' for result in results]), 'Get error'

    def test_sai_macsec_attr_stag_tpid_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_stag_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': ['SAI_MACSEC_ATTR_STAG_TPID', '0x88A8'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_attr_stag_tpid_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_stag_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_STAG_TPID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x88A8' for result in results]), 'Get error'

    def test_sai_macsec_attr_max_vlan_tags_parsed_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_max_vlan_tags_parsed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': ['SAI_MACSEC_ATTR_MAX_VLAN_TAGS_PARSED', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_attr_max_vlan_tags_parsed_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_max_vlan_tags_parsed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_MAX_VLAN_TAGS_PARSED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_macsec_attr_stats_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_stats_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': [
                    'SAI_MACSEC_ATTR_STATS_MODE',
                    'SAI_STATS_MODE_READ_AND_CLEAR',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_attr_stats_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_stats_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_STATS_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATS_MODE_READ_AND_CLEAR' for result in results]
        ), 'Get error'

    def test_sai_macsec_attr_physical_bypass_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_physical_bypass_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': ['SAI_MACSEC_ATTR_PHYSICAL_BYPASS_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_attr_physical_bypass_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_physical_bypass_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_PHYSICAL_BYPASS_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_macsec_attr_supported_port_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_supported_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_SUPPORTED_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_available_macsec_flow_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_available_macsec_flow_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_AVAILABLE_MACSEC_FLOW',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_flow_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_flow_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_FLOW_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_available_macsec_sc_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_available_macsec_sc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_AVAILABLE_MACSEC_SC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_available_macsec_sa_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_available_macsec_sa_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_AVAILABLE_MACSEC_SA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_attr_max_secure_associations_per_sc_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_attr_max_secure_associations_per_sc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'atrribute': 'SAI_MACSEC_ATTR_MAX_SECURE_ASSOCIATIONS_PER_SC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_macsec_remove(self, npu):
        commands = [
            {
                'name': 'macsec_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'attributes': [
                    'SAI_MACSEC_ATTR_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
