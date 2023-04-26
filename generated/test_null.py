

from pprint import pprint

import pytest


class TestSaiNull:

    @pytest.mark.dependency(scope='session')
    def test_null_create(self, npu):

        commands = [{'name': 'null_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NULL', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_null_remove(self, npu):

        commands = [{'name': 'null_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_NULL', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

