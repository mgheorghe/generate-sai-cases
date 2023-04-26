

from pprint import pprint

import pytest

# object with no attributes
class TestSaiHash:

    @pytest.mark.dependency(scope='session')
    def test_hash_create(self, npu):

        commands = [{'name': 'hash_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HASH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_hash_remove(self, npu):

        commands = [{'name': 'hash_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HASH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

