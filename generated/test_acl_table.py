
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiAclTable:
    # object with no parents

    def test_acl_table_create(self, npu):

        commands = [{'name': 'acl_table_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ACL_TABLE', 'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_acl_table_attr_entry_list_get(self, npu):

        commands = [
            {
                "name": "acl_table_1",
                "op": "get",
                "attributes": ["SAI_ACL_TABLE_ATTR_ENTRY_LIST"]
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


    
    def test_sai_acl_table_attr_available_acl_entry_get(self, npu):

        commands = [
            {
                "name": "acl_table_1",
                "op": "get",
                "attributes": ["SAI_ACL_TABLE_ATTR_AVAILABLE_ACL_ENTRY"]
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


    
    def test_sai_acl_table_attr_available_acl_counter_get(self, npu):

        commands = [
            {
                "name": "acl_table_1",
                "op": "get",
                "attributes": ["SAI_ACL_TABLE_ATTR_AVAILABLE_ACL_COUNTER"]
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


    def test_acl_table_remove(self, npu):

        commands = [{'name': 'acl_table_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

