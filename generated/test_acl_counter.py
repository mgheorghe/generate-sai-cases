

from pprint import pprint

import pytest


class TestSaiAclCounter:

    @pytest.mark.dependency(scope='session')
    def test_acl_counter_create(self, npu):

        commands = [{'name': 'acl_counter_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ACL_COUNTER', 'attributes': ['SAI_ACL_COUNTER_ATTR_TABLE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_acl_counter_remove(self, npu):

        commands = [{'name': 'acl_counter_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_ACL_COUNTER', 'attributes': ['SAI_ACL_COUNTER_ATTR_TABLE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
