

from pprint import pprint

import pytest


class TestSaiNextHopGroupMember:

    @pytest.mark.dependency(scope='session')
    def test_next_hop_group_member_create(self, npu):

        commands = [{'name': 'next_hop_group_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MEMBER', 'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_GROUP_ID', 'sai_object_id_t', 'SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_next_hop_group_member_remove(self, npu):

        commands = [{'name': 'next_hop_group_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MEMBER', 'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_GROUP_ID', 'sai_object_id_t', 'SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

