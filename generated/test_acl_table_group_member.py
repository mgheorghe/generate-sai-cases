

from pprint import pprint

import pytest


class TestSaiAclTableGroupMember:

    @pytest.mark.dependency(scope='session')
    def test_acl_table_group_member_create(self, npu):

        commands = [{'name': 'acl_table_group_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP_MEMBER', 'attributes': ['SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_GROUP_ID', 'sai_object_id_t', 'SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_ID', 'sai_object_id_t', 'SAI_ACL_TABLE_GROUP_MEMBER_ATTR_PRIORITY', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_acl_table_group_member_remove(self, npu):

        commands = [{'name': 'acl_table_group_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP_MEMBER', 'attributes': ['SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_GROUP_ID', 'sai_object_id_t', 'SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_ID', 'sai_object_id_t', 'SAI_ACL_TABLE_GROUP_MEMBER_ATTR_PRIORITY', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

