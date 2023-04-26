

from pprint import pprint

import pytest

# object with no attributes
class TestSaiDirectionLookupEntry:

    @pytest.mark.dependency(scope='session')
    def test_direction_lookup_entry_create(self, npu):

        commands = [{'name': 'direction_lookup_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_direction_lookup_entry_remove(self, npu):

        commands = [{'name': 'direction_lookup_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

