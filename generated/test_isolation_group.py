

from pprint import pprint

import pytest


class TestSaiIsolationGroup:

    @pytest.mark.dependency(scope='session')
    def test_isolation_group_create(self, npu):

        commands = [{'name': 'isolation_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP', 'attributes': ['SAI_ISOLATION_GROUP_ATTR_TYPE', 'sai_isolation_group_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_isolation_group_remove(self, npu):

        commands = [{'name': 'isolation_group_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP', 'attributes': ['SAI_ISOLATION_GROUP_ATTR_TYPE', 'sai_isolation_group_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

