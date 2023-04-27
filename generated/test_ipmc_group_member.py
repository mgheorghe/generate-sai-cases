

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_IPMC_GROUP SAI_OBJECT_TYPE_ROUTER_INTERFACE, SAI_OBJECT_TYPE_TUNNEL
class TestSaiIpmcGroupMember:

    @pytest.mark.dependency(scope='session')
    def test_ipmc_group_member_create(self, npu):

        commands = [{'name': 'ipmc_group_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_IPMC_GROUP_MEMBER', 'attributes': ['SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_GROUP_ID', 'sai_object_id_t', 'SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_OUTPUT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_ipmc_group_member_remove(self, npu):

        commands = [{'name': 'ipmc_group_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_IPMC_GROUP_MEMBER', 'attributes': ['SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_GROUP_ID', 'sai_object_id_t', 'SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_OUTPUT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
