

from pprint import pprint

import pytest


class TestSaiUdf:

    @pytest.mark.dependency(scope='session')
    def test_udf_create(self, npu):

        commands = [{'name': 'udf_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_UDF', 'attributes': ['SAI_UDF_ATTR_MATCH_ID', 'sai_object_id_t', 'SAI_UDF_ATTR_GROUP_ID', 'sai_object_id_t', 'SAI_UDF_ATTR_OFFSET', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_udf_remove(self, npu):

        commands = [{'name': 'udf_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_UDF', 'attributes': ['SAI_UDF_ATTR_MATCH_ID', 'sai_object_id_t', 'SAI_UDF_ATTR_GROUP_ID', 'sai_object_id_t', 'SAI_UDF_ATTR_OFFSET', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

