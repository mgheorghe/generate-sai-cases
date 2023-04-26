

from pprint import pprint

import pytest


class TestSaiDashAclGroup:

    @pytest.mark.dependency(scope='session')
    def test_dash_acl_group_create(self, npu):

        commands = [{'name': 'dash_acl_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_dash_acl_group_remove(self, npu):

        commands = [{'name': 'dash_acl_group_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

