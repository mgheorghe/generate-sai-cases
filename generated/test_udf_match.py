

from pprint import pprint

import pytest


class TestSaiUdfMatch:

    @pytest.mark.dependency(scope='session')
    def test_udf_match_create(self, npu):

        commands = [{'name': 'udf_match_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_UDF_MATCH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_udf_match_remove(self, npu):

        commands = [{'name': 'udf_match_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_UDF_MATCH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

