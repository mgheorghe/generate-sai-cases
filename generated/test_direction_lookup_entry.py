

from pprint import pprint

import pytest


class TestSaiDirectionLookupEntry:

    @pytest.mark.dependency(scope='session')
    def test_direction_lookup_entry_create(self, npu):

        commands = [{'name': 'direction_lookup_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_direction_lookup_entry_remove(self, npu):

        commands = [{'name': 'direction_lookup_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

