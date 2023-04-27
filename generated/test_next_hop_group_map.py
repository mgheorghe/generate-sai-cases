

from pprint import pprint

import pytest

# object with no parents
class TestSaiNextHopGroupMap:

    @pytest.mark.dependency(scope='session')
    def test_next_hop_group_map_create(self, npu):

        commands = [{'name': 'next_hop_group_map_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MAP', 'attributes': ['SAI_NEXT_HOP_GROUP_MAP_ATTR_TYPE', 'SAI_NEXT_HOP_GROUP_MAP_TYPE_FORWARDING_CLASS_TO_INDEX']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_next_hop_group_map_remove(self, npu):

        commands = [{'name': 'next_hop_group_map_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MAP', 'attributes': ['SAI_NEXT_HOP_GROUP_MAP_ATTR_TYPE', 'SAI_NEXT_HOP_GROUP_MAP_TYPE_FORWARDING_CLASS_TO_INDEX']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
