

from pprint import pprint

import pytest


class TestSaiNeighborEntry:

    @pytest.mark.dependency(scope='session')
    def test_neighbor_entry_create(self, npu):

        commands = [{'name': 'neighbor_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY', 'attributes': ['SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS', 'sai_mac_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_neighbor_entry_remove(self, npu):

        commands = [{'name': 'neighbor_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY', 'attributes': ['SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS', 'sai_mac_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
