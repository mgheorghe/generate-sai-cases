

from pprint import pprint

import pytest

# object with no attributes
class TestSaiDashAclGroup:

    @pytest.mark.dependency(scope='session')
    def test_dash_acl_group_create(self, npu):

        commands = [{'name': 'dash_acl_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_dash_acl_group_remove(self, npu):

        commands = [{'name': 'dash_acl_group_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

