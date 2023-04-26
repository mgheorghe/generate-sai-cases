

from pprint import pprint

import pytest


class TestSaiRpfGroupMember:

    @pytest.mark.dependency(scope='session')
    def test_rpf_group_member_create(self, npu):

        commands = [{'name': 'rpf_group_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_RPF_GROUP_MEMBER', 'attributes': ['SAI_RPF_GROUP_MEMBER_ATTR_RPF_GROUP_ID', 'sai_object_id_t', 'SAI_RPF_GROUP_MEMBER_ATTR_RPF_INTERFACE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_rpf_group_member_remove(self, npu):

        commands = [{'name': 'rpf_group_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_RPF_GROUP_MEMBER', 'attributes': ['SAI_RPF_GROUP_MEMBER_ATTR_RPF_GROUP_ID', 'sai_object_id_t', 'SAI_RPF_GROUP_MEMBER_ATTR_RPF_INTERFACE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

