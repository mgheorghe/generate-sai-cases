from pprint import pprint

import pytest


class TestSaiIpsec:
    # object with no parents

    def test_ipsec_create(self, npu):
        commands = [
            {
                'name': 'ipsec_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'attributes': ['SAI_IPSEC_ATTR_EXTERNAL_SA_INDEX_ENABLE', 'True'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_ipsec_attr_term_remote_ip_match_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_term_remote_ip_match_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_TERM_REMOTE_IP_MATCH_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_switching_mode_cut_through_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_switching_mode_cut_through_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_SWITCHING_MODE_CUT_THROUGH_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_switching_mode_store_and_forward_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_switching_mode_store_and_forward_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_SWITCHING_MODE_STORE_AND_FORWARD_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_stats_mode_read_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_stats_mode_read_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_STATS_MODE_READ_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_stats_mode_read_clear_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_stats_mode_read_clear_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_STATS_MODE_READ_CLEAR_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_sn_32bit_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_sn_32bit_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_SN_32BIT_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_esn_64bit_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_esn_64bit_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_ESN_64BIT_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_supported_cipher_list_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_supported_cipher_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_SUPPORTED_CIPHER_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_system_side_mtu_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_system_side_mtu_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_SYSTEM_SIDE_MTU',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_warm_boot_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_warm_boot_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_WARM_BOOT_SUPPORTED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_warm_boot_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_warm_boot_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': ['SAI_IPSEC_ATTR_WARM_BOOT_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_attr_warm_boot_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_warm_boot_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_WARM_BOOT_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_ipsec_attr_ctag_tpid_set(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_ctag_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': ['SAI_IPSEC_ATTR_CTAG_TPID', '0x8100'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_attr_ctag_tpid_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_ctag_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_CTAG_TPID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x8100' for result in results]), 'Get error'

    def test_sai_ipsec_attr_stag_tpid_set(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_stag_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': ['SAI_IPSEC_ATTR_STAG_TPID', '0x88A8'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_attr_stag_tpid_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_stag_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_STAG_TPID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x88A8' for result in results]), 'Get error'

    def test_sai_ipsec_attr_max_vlan_tags_parsed_set(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_max_vlan_tags_parsed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': ['SAI_IPSEC_ATTR_MAX_VLAN_TAGS_PARSED', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_attr_max_vlan_tags_parsed_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_max_vlan_tags_parsed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_MAX_VLAN_TAGS_PARSED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ipsec_attr_octet_count_high_watermark_set(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_octet_count_high_watermark_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': ['SAI_IPSEC_ATTR_OCTET_COUNT_HIGH_WATERMARK', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_attr_octet_count_high_watermark_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_octet_count_high_watermark_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_OCTET_COUNT_HIGH_WATERMARK',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ipsec_attr_octet_count_low_watermark_set(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_octet_count_low_watermark_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': ['SAI_IPSEC_ATTR_OCTET_COUNT_LOW_WATERMARK', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_attr_octet_count_low_watermark_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_octet_count_low_watermark_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_OCTET_COUNT_LOW_WATERMARK',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ipsec_attr_stats_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_stats_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': [
                    'SAI_IPSEC_ATTR_STATS_MODE',
                    'SAI_STATS_MODE_READ_AND_CLEAR',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_attr_stats_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_stats_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_STATS_MODE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATS_MODE_READ_AND_CLEAR' for result in results]
        ), 'Get error'

    def test_sai_ipsec_attr_available_ipsec_sa_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_available_ipsec_sa_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_AVAILABLE_IPSEC_SA',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipsec_attr_sa_list_get(self, npu):
        commands = [
            {
                'name': 'sai_ipsec_attr_sa_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'atrribute': 'SAI_IPSEC_ATTR_SA_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_ipsec_remove(self, npu):
        commands = [
            {
                'name': 'ipsec_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'attributes': ['SAI_IPSEC_ATTR_EXTERNAL_SA_INDEX_ENABLE', 'True'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
