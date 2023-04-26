

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_DASH_ACL_GROUP
class TestSaiDashAclRule:

    @pytest.mark.dependency(scope='session')
    def test_dash_acl_rule_create(self, npu):

        commands = [{'name': 'dash_acl_rule_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE', 'attributes': ['SAI_DASH_ACL_RULE_ATTR_DASH_ACL_GROUP_ID', 'sai_object_id_t', 'SAI_DASH_ACL_RULE_ATTR_DIP', 'sai_ip_prefix_list_t', 'SAI_DASH_ACL_RULE_ATTR_SIP', 'sai_ip_prefix_list_t', 'SAI_DASH_ACL_RULE_ATTR_PROTOCOL', 'sai_u8_list_t', 'SAI_DASH_ACL_RULE_ATTR_SRC_PORT', 'sai_u16_range_list_t', 'SAI_DASH_ACL_RULE_ATTR_DST_PORT', 'sai_u16_range_list_t', 'SAI_DASH_ACL_RULE_ATTR_PRIORITY', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_dash_acl_rule_remove(self, npu):

        commands = [{'name': 'dash_acl_rule_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE', 'attributes': ['SAI_DASH_ACL_RULE_ATTR_DASH_ACL_GROUP_ID', 'sai_object_id_t', 'SAI_DASH_ACL_RULE_ATTR_DIP', 'sai_ip_prefix_list_t', 'SAI_DASH_ACL_RULE_ATTR_SIP', 'sai_ip_prefix_list_t', 'SAI_DASH_ACL_RULE_ATTR_PROTOCOL', 'sai_u8_list_t', 'SAI_DASH_ACL_RULE_ATTR_SRC_PORT', 'sai_u16_range_list_t', 'SAI_DASH_ACL_RULE_ATTR_DST_PORT', 'sai_u16_range_list_t', 'SAI_DASH_ACL_RULE_ATTR_PRIORITY', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

