

from pprint import pprint

import pytest

# object with no attributes
class TestSaiNextHopGroupMap:

    @pytest.mark.dependency(scope='session')
    def test_next_hop_group_map_create(self, npu):

        commands = [{'name': 'next_hop_group_map_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MAP', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_next_hop_group_map_remove(self, npu):

        commands = [{'name': 'next_hop_group_map_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MAP', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

