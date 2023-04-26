

from pprint import pprint

import pytest


class TestSaiDashAclRule:

    @pytest.mark.dependency(scope='session')
    def test_dash_acl_rule_create(self, npu):

        commands = [{'name': 'dash_acl_rule_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_dash_acl_rule_remove(self, npu):

        commands = [{'name': 'dash_acl_rule_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

