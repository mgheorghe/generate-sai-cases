

from pprint import pprint

import pytest

# object with no attributes
class TestSaiFineGrainedHashField:

    @pytest.mark.dependency(scope='session')
    def test_fine_grained_hash_field_create(self, npu):

        commands = [{'name': 'fine_grained_hash_field_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_FINE_GRAINED_HASH_FIELD', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_fine_grained_hash_field_remove(self, npu):

        commands = [{'name': 'fine_grained_hash_field_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_FINE_GRAINED_HASH_FIELD', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

