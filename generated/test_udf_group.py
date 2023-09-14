
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiUdfGroup:
    # object with no parents

    def test_udf_group_create(self, npu):

        commands = [{'name': 'udf_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_UDF_GROUP', 'attributes': ['SAI_UDF_GROUP_ATTR_LENGTH', '10']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_udf_group_attr_udf_list_get(self, npu):

        commands = [
            {
                "name": "udf_group_1",
                "op": "get",
                "attributes": ["SAI_UDF_GROUP_ATTR_UDF_LIST"]
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


    def test_udf_group_remove(self, npu):

        commands = [{'name': 'udf_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

