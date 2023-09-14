
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiIpmcGroup:
    # object with no attributes

    def test_ipmc_group_create(self, npu):

        commands = [{'name': 'ipmc_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_IPMC_GROUP', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_ipmc_group_attr_ipmc_output_count_get(self, npu):

        commands = [
            {
                "name": "ipmc_group_1",
                "op": "get",
                "attributes": ["SAI_IPMC_GROUP_ATTR_IPMC_OUTPUT_COUNT"]
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


    
    def test_sai_ipmc_group_attr_ipmc_member_list_get(self, npu):

        commands = [
            {
                "name": "ipmc_group_1",
                "op": "get",
                "attributes": ["SAI_IPMC_GROUP_ATTR_IPMC_MEMBER_LIST"]
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


    def test_ipmc_group_remove(self, npu):

        commands = [{'name': 'ipmc_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

