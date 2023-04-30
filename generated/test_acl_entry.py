from pprint import pprint

import pytest


class TestSaiAclEntry:
    # object with parent SAI_OBJECT_TYPE_ACL_TABLE

    def test_acl_entry_create(self, npu):
        commands = [
            {
                'name': 'acl_table_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS'],
            },
            {
                'name': 'acl_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'attributes': ['SAI_ACL_ENTRY_ATTR_TABLE_ID', '$acl_table_1'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_acl_entry_attr_priority_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_PRIORITY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_admin_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ADMIN_STATE', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_admin_state_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_admin_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ADMIN_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word3_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word3_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD3', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word3_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word3_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD3',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word2_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word2_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD2', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word2_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word2_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD2',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word1_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word1_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD1', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word1_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word1_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD1',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word0_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word0_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD0', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ipv6_word0_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ipv6_word0_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_IPV6_WORD0',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word3_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word3_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD3', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word3_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word3_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD3',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word2_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word2_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD2', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word2_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word2_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD2',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word1_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word1_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD1', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word1_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word1_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD1',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word0_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word0_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD0', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ipv6_word0_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ipv6_word0_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DST_IPV6_WORD0',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_src_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_src_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_SRC_IPV6', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_src_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_src_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_SRC_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_dst_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_dst_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_DST_IPV6', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_dst_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_dst_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_DST_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_mac_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_mac_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_MAC', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_mac_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_mac_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_MAC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_mac_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_mac_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DST_MAC', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_mac_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_mac_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DST_MAC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ip_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_IP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_ip_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ip_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DST_IP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dst_ip_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dst_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DST_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_src_ip_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_src_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_SRC_IP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_src_ip_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_src_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_SRC_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_dst_ip_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_dst_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_DST_IP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_dst_ip_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_dst_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_DST_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_in_ports_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_in_ports_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_IN_PORTS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_in_ports_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_in_ports_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_IN_PORTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_out_ports_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_out_ports_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_OUT_PORTS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_out_ports_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_out_ports_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_OUT_PORTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_in_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_in_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_IN_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_in_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_in_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_IN_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_out_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_out_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_OUT_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_out_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_out_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_OUT_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_SRC_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_src_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_src_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_SRC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_outer_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_outer_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_OUTER_VLAN_ID', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_outer_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_outer_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_OUTER_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_outer_vlan_pri_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_outer_vlan_pri_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_OUTER_VLAN_PRI', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_outer_vlan_pri_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_outer_vlan_pri_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_OUTER_VLAN_PRI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_outer_vlan_cfi_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_outer_vlan_cfi_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_OUTER_VLAN_CFI', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_outer_vlan_cfi_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_outer_vlan_cfi_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_OUTER_VLAN_CFI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_VLAN_ID', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_vlan_pri_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_vlan_pri_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_VLAN_PRI', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_vlan_pri_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_vlan_pri_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_VLAN_PRI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_vlan_cfi_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_vlan_cfi_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_VLAN_CFI', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_vlan_cfi_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_vlan_cfi_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_VLAN_CFI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_l4_src_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_l4_src_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_L4_SRC_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_l4_src_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_l4_src_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_L4_SRC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_l4_dst_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_l4_dst_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_L4_DST_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_l4_dst_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_l4_dst_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_L4_DST_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_l4_src_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_l4_src_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_L4_SRC_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_l4_src_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_l4_src_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_L4_SRC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_l4_dst_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_l4_dst_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_L4_DST_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_l4_dst_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_l4_dst_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_L4_DST_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ether_type_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ether_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ETHER_TYPE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ether_type_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ether_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ETHER_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_ether_type_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_ether_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_ETHER_TYPE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_ether_type_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_ether_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_ETHER_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ip_protocol_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ip_protocol_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_IP_PROTOCOL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ip_protocol_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ip_protocol_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_IP_PROTOCOL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_ip_protocol_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_ip_protocol_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_INNER_IP_PROTOCOL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_inner_ip_protocol_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_inner_ip_protocol_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_INNER_IP_PROTOCOL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ip_identification_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ip_identification_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_IP_IDENTIFICATION', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ip_identification_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ip_identification_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_IP_IDENTIFICATION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dscp_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dscp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_DSCP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_dscp_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_dscp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_DSCP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ecn_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ecn_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ECN', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ecn_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ecn_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ECN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_TTL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tos_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_TOS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tos_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_TOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ip_flags_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ip_flags_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_IP_FLAGS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ip_flags_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ip_flags_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_IP_FLAGS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tcp_flags_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tcp_flags_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_TCP_FLAGS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tcp_flags_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tcp_flags_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_TCP_FLAGS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_ip_type_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_ip_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ACL_IP_TYPE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_ip_type_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_ip_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ACL_IP_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_ip_frag_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_ip_frag_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ACL_IP_FRAG', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_ip_frag_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_ip_frag_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ACL_IP_FRAG',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ipv6_flow_label_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ipv6_flow_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_IPV6_FLOW_LABEL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ipv6_flow_label_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ipv6_flow_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_IPV6_FLOW_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tc_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_TC', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tc_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmp_type_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmp_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ICMP_TYPE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmp_type_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmp_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ICMP_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmp_code_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmp_code_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ICMP_CODE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmp_code_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmp_code_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ICMP_CODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmpv6_type_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmpv6_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ICMPV6_TYPE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmpv6_type_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmpv6_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ICMPV6_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmpv6_code_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmpv6_code_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ICMPV6_CODE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_icmpv6_code_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_icmpv6_code_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ICMPV6_CODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_packet_vlan_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_packet_vlan_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_PACKET_VLAN', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_packet_vlan_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_packet_vlan_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_PACKET_VLAN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tunnel_vni_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tunnel_vni_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_TUNNEL_VNI', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tunnel_vni_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tunnel_vni_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_TUNNEL_VNI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_has_vlan_tag_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_has_vlan_tag_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_HAS_VLAN_TAG', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_has_vlan_tag_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_has_vlan_tag_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_HAS_VLAN_TAG',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_macsec_sci_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_macsec_sci_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MACSEC_SCI', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_macsec_sci_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_macsec_sci_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MACSEC_SCI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_label_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_LABEL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_label_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_TTL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_exp_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_exp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_EXP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_exp_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_exp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_EXP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_bos_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_bos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_BOS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label0_bos_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label0_bos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL0_BOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_label_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_LABEL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_label_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_TTL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_exp_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_exp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_EXP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_exp_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_exp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_EXP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_bos_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_bos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_BOS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label1_bos_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label1_bos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL1_BOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_label_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_LABEL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_label_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_TTL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_exp_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_exp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_EXP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_exp_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_exp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_EXP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_bos_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_bos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_BOS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label2_bos_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label2_bos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL2_BOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_label_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_LABEL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_label_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_TTL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_exp_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_exp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_EXP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_exp_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_exp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_EXP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_bos_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_bos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_BOS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label3_bos_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label3_bos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL3_BOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_label_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_LABEL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_label_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_TTL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_exp_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_exp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_EXP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_exp_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_exp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_EXP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_bos_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_bos_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_BOS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_mpls_label4_bos_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_mpls_label4_bos_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_MPLS_LABEL4_BOS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_fdb_dst_user_meta_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_fdb_dst_user_meta_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_FDB_DST_USER_META', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_fdb_dst_user_meta_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_fdb_dst_user_meta_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_FDB_DST_USER_META',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_route_dst_user_meta_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_route_dst_user_meta_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_FIELD_ROUTE_DST_USER_META',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_route_dst_user_meta_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_route_dst_user_meta_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ROUTE_DST_USER_META',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_neighbor_dst_user_meta_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_neighbor_dst_user_meta_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_FIELD_NEIGHBOR_DST_USER_META',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_neighbor_dst_user_meta_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_neighbor_dst_user_meta_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_NEIGHBOR_DST_USER_META',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_port_user_meta_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_port_user_meta_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_PORT_USER_META', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_port_user_meta_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_port_user_meta_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_PORT_USER_META',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_vlan_user_meta_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_vlan_user_meta_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_VLAN_USER_META', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_vlan_user_meta_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_vlan_user_meta_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_VLAN_USER_META',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_user_meta_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_user_meta_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ACL_USER_META', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_user_meta_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_user_meta_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ACL_USER_META',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_fdb_npu_meta_dst_hit_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_fdb_npu_meta_dst_hit_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_FIELD_FDB_NPU_META_DST_HIT',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_fdb_npu_meta_dst_hit_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_fdb_npu_meta_dst_hit_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_FDB_NPU_META_DST_HIT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_neighbor_npu_meta_dst_hit_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_neighbor_npu_meta_dst_hit_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_FIELD_NEIGHBOR_NPU_META_DST_HIT',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_neighbor_npu_meta_dst_hit_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_neighbor_npu_meta_dst_hit_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_NEIGHBOR_NPU_META_DST_HIT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_route_npu_meta_dst_hit_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_route_npu_meta_dst_hit_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_FIELD_ROUTE_NPU_META_DST_HIT',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_route_npu_meta_dst_hit_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_route_npu_meta_dst_hit_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ROUTE_NPU_META_DST_HIT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_bth_opcode_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_bth_opcode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_BTH_OPCODE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_bth_opcode_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_bth_opcode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_BTH_OPCODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_aeth_syndrome_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_aeth_syndrome_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_AETH_SYNDROME', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_aeth_syndrome_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_aeth_syndrome_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_AETH_SYNDROME',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_user_defined_field_group_min_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_user_defined_field_group_min_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_USER_DEFINED_FIELD_GROUP_MIN',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_user_defined_field_group_min_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_user_defined_field_group_min_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_USER_DEFINED_FIELD_GROUP_MIN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_user_defined_field_group_max_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_user_defined_field_group_max_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_USER_DEFINED_FIELD_GROUP_MAX',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_user_defined_field_group_max_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_user_defined_field_group_max_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_USER_DEFINED_FIELD_GROUP_MAX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_range_type_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_range_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_ACL_RANGE_TYPE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_acl_range_type_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_acl_range_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_ACL_RANGE_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ipv6_next_header_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ipv6_next_header_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_IPV6_NEXT_HEADER', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_ipv6_next_header_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_ipv6_next_header_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_IPV6_NEXT_HEADER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_gre_key_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_gre_key_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_GRE_KEY', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_gre_key_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_gre_key_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_GRE_KEY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tam_int_type_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tam_int_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_FIELD_TAM_INT_TYPE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_field_tam_int_type_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_field_tam_int_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_FIELD_TAM_INT_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_redirect_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_redirect_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_REDIRECT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_redirect_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_redirect_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_REDIRECT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_endpoint_ip_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_endpoint_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_ENDPOINT_IP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_endpoint_ip_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_endpoint_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_ENDPOINT_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_redirect_list_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_redirect_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_REDIRECT_LIST', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_redirect_list_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_redirect_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_REDIRECT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_PACKET_ACTION', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_flood_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_flood_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_FLOOD', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_flood_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_flood_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_FLOOD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_counter_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_counter_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_COUNTER', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_counter_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_counter_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_COUNTER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_mirror_ingress_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_mirror_ingress_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_INGRESS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_mirror_ingress_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_mirror_ingress_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_INGRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_mirror_egress_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_mirror_egress_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_EGRESS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_mirror_egress_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_mirror_egress_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_MIRROR_EGRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_policer_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_policer_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_POLICER', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_policer_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_policer_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_POLICER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_decrement_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_decrement_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_DECREMENT_TTL', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_decrement_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_decrement_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_DECREMENT_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_tc_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_TC', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_tc_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_packet_color_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_packet_color_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_PACKET_COLOR', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_packet_color_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_packet_color_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_PACKET_COLOR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_inner_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_inner_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_INNER_VLAN_ID',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_inner_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_inner_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_INNER_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_inner_vlan_pri_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_inner_vlan_pri_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_INNER_VLAN_PRI',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_inner_vlan_pri_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_inner_vlan_pri_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_INNER_VLAN_PRI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_outer_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_outer_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_OUTER_VLAN_ID',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_outer_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_outer_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_OUTER_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_outer_vlan_pri_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_outer_vlan_pri_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_OUTER_VLAN_PRI',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_outer_vlan_pri_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_outer_vlan_pri_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_OUTER_VLAN_PRI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_add_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_add_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_ADD_VLAN_ID', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_add_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_add_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_ADD_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_add_vlan_pri_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_add_vlan_pri_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_ADD_VLAN_PRI', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_add_vlan_pri_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_add_vlan_pri_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_ADD_VLAN_PRI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_src_mac_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_src_mac_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_SRC_MAC', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_src_mac_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_src_mac_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_SRC_MAC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dst_mac_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dst_mac_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_DST_MAC', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dst_mac_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dst_mac_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_DST_MAC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_src_ip_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_src_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_SRC_IP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_src_ip_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_src_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_SRC_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dst_ip_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dst_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_DST_IP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dst_ip_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dst_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_DST_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_src_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_src_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_SRC_IPV6', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_src_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_src_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_SRC_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dst_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dst_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_DST_IPV6', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dst_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dst_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_DST_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dscp_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dscp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_DSCP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_dscp_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_dscp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_DSCP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ecn_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ecn_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_ECN', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ecn_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ecn_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_ECN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_l4_src_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_l4_src_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_L4_SRC_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_l4_src_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_l4_src_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_L4_SRC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_l4_dst_port_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_l4_dst_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_L4_DST_PORT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_l4_dst_port_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_l4_dst_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_L4_DST_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_ingress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_ingress_samplepacket_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_INGRESS_SAMPLEPACKET_ENABLE',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_ingress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_ingress_samplepacket_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_INGRESS_SAMPLEPACKET_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_egress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_egress_samplepacket_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_EGRESS_SAMPLEPACKET_ENABLE',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_egress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_egress_samplepacket_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_EGRESS_SAMPLEPACKET_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_acl_meta_data_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_acl_meta_data_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_ACL_META_DATA',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_acl_meta_data_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_acl_meta_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_ACL_META_DATA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_egress_block_port_list_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_egress_block_port_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_EGRESS_BLOCK_PORT_LIST',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_egress_block_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_egress_block_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_EGRESS_BLOCK_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_user_trap_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_user_trap_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_USER_TRAP_ID', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_user_trap_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_user_trap_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_USER_TRAP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_do_not_learn_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_do_not_learn_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_DO_NOT_LEARN', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_do_not_learn_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_do_not_learn_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_DO_NOT_LEARN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_acl_dtel_flow_op_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_acl_dtel_flow_op_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_ACL_DTEL_FLOW_OP', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_acl_dtel_flow_op_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_acl_dtel_flow_op_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_ACL_DTEL_FLOW_OP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_int_session_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_int_session_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_DTEL_INT_SESSION', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_int_session_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_int_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_INT_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_drop_report_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_drop_report_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_DROP_REPORT_ENABLE',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_drop_report_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_drop_report_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_DROP_REPORT_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_tail_drop_report_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_tail_drop_report_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_TAIL_DROP_REPORT_ENABLE',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_tail_drop_report_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_tail_drop_report_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_TAIL_DROP_REPORT_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_flow_sample_percent_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_flow_sample_percent_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_FLOW_SAMPLE_PERCENT',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_flow_sample_percent_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_flow_sample_percent_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_FLOW_SAMPLE_PERCENT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_report_all_packets_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_report_all_packets_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_REPORT_ALL_PACKETS',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_dtel_report_all_packets_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_dtel_report_all_packets_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_DTEL_REPORT_ALL_PACKETS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_no_nat_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_no_nat_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_NO_NAT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_no_nat_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_no_nat_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_NO_NAT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_insert_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_insert_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_INT_INSERT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_insert_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_insert_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_INT_INSERT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_delete_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_delete_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_INT_DELETE', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_delete_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_delete_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_INT_DELETE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_report_flow_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_report_flow_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_INT_REPORT_FLOW', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_report_flow_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_report_flow_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_INT_REPORT_FLOW',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_report_drops_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_report_drops_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_INT_REPORT_DROPS', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_report_drops_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_report_drops_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_INT_REPORT_DROPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_report_tail_drops_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_report_tail_drops_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_INT_REPORT_TAIL_DROPS',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_int_report_tail_drops_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_int_report_tail_drops_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_INT_REPORT_TAIL_DROPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_tam_int_object_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_tam_int_object_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_TAM_INT_OBJECT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_tam_int_object_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_tam_int_object_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_TAM_INT_OBJECT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_isolation_group_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_isolation_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_ISOLATION_GROUP',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_isolation_group_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_isolation_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_ISOLATION_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_macsec_flow_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_macsec_flow_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_MACSEC_FLOW', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_macsec_flow_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_macsec_flow_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_MACSEC_FLOW',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_lag_hash_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_lag_hash_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_LAG_HASH_ID', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_lag_hash_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_lag_hash_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_LAG_HASH_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ecmp_hash_id_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ecmp_hash_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_ECMP_HASH_ID', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ecmp_hash_id_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ecmp_hash_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_ECMP_HASH_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_vrf_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_vrf_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_VRF', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_vrf_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_vrf_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_VRF',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_forwarding_class_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_forwarding_class_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_FORWARDING_CLASS',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_forwarding_class_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_forwarding_class_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_FORWARDING_CLASS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ars_monitoring_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ars_monitoring_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_SET_ARS_MONITORING',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ars_monitoring_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ars_monitoring_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_ARS_MONITORING',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ars_object_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ars_object_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': ['SAI_ACL_ENTRY_ATTR_ACTION_SET_ARS_OBJECT', 'disabled'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_set_ars_object_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_set_ars_object_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_SET_ARS_OBJECT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_disable_ars_forwarding_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_disable_ars_forwarding_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': [
                    'SAI_ACL_ENTRY_ATTR_ACTION_DISABLE_ARS_FORWARDING',
                    'disabled',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_entry_attr_action_disable_ars_forwarding_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_entry_attr_action_disable_ars_forwarding_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'atrribute': 'SAI_ACL_ENTRY_ATTR_ACTION_DISABLE_ARS_FORWARDING',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'disabled' for result in results]), 'Get error'

    def test_acl_entry_remove(self, npu):
        commands = [
            {
                'name': 'acl_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'attributes': ['SAI_ACL_ENTRY_ATTR_TABLE_ID', '$acl_table_1'],
            },
            {
                'name': 'acl_table_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
