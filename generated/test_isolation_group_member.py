

from pprint import pprint

import pytest


class TestSaiIsolationGroupMember:

    @pytest.mark.dependency(scope='session')
    def test_isolation_group_member_create(self, npu):

        commands = [{'name': 'isolation_group_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP_MEMBER', 'attributes': ['SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_GROUP_ID', 'sai_object_id_t', 'SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_OBJECT', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_isolation_group_member_remove(self, npu):

        commands = [{'name': 'isolation_group_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP_MEMBER', 'attributes': ['SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_GROUP_ID', 'sai_object_id_t', 'SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_OBJECT', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

