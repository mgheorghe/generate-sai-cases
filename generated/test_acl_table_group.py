
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiAclTableGroup:
    # object with no parents

    def test_acl_table_group_create(self, npu):

        commands = [{'name': 'acl_table_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP', 'attributes': ['SAI_ACL_TABLE_GROUP_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_acl_table_group_attr_member_list_get(self, npu):

        commands = [
            {
                "name": "acl_table_group_1",
                "op": "get",
                "attributes": ["SAI_ACL_TABLE_GROUP_ATTR_MEMBER_LIST"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    
    def test_sai_acl_table_group_attr_chain_group_list_get(self, npu):

        commands = [
            {
                "name": "acl_table_group_1",
                "op": "get",
                "attributes": ["SAI_ACL_TABLE_GROUP_ATTR_CHAIN_GROUP_LIST"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    def test_acl_table_group_remove(self, npu):

        commands = [{'name': 'acl_table_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

