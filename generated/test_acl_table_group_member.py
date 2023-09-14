
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiAclTableGroupMember:
    # object with parent SAI_OBJECT_TYPE_ACL_TABLE_GROUP SAI_OBJECT_TYPE_ACL_TABLE

    def test_acl_table_group_member_create(self, npu):

        commands = [{'name': 'acl_table_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP', 'attributes': ['SAI_ACL_TABLE_GROUP_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS']}, {'name': 'acl_table_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ACL_TABLE', 'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS']}, {'name': 'acl_table_group_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP_MEMBER', 'attributes': ['SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_GROUP_ID', '$acl_table_group_1', 'SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_ID', '$acl_table_1', 'SAI_ACL_TABLE_GROUP_MEMBER_ATTR_PRIORITY', '10']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_acl_table_group_member_attr_acl_table_chain_group_id_set")
    def test_sai_acl_table_group_member_attr_acl_table_chain_group_id_set(self, npu):

        commands = [
            {
                "name": "acl_table_group_member_1",
                "op": "set",
                "attributes": ["SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_CHAIN_GROUP_ID", 'null']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_acl_table_group_member_attr_acl_table_chain_group_id_set"])
    def test_sai_acl_table_group_member_attr_acl_table_chain_group_id_get(self, npu):

        commands = [
            {
                "name": "acl_table_group_member_1",
                "op": "get",
                "attributes": ["SAI_ACL_TABLE_GROUP_MEMBER_ATTR_ACL_TABLE_CHAIN_GROUP_ID"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' %  r_value


    def test_acl_table_group_member_remove(self, npu):

        commands = [{'name': 'acl_table_group_member_1', 'op': 'remove'}, {'name': 'acl_table_1', 'op': 'remove'}, {'name': 'acl_table_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

