

from pprint import pprint

import pytest


class TestSaiLagMember:

    @pytest.mark.dependency(scope='session')
    def test_lag_member_create(self, npu):

        commands = [{'name': 'lag_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_LAG_MEMBER', 'attributes': ['SAI_LAG_MEMBER_ATTR_LAG_ID', 'sai_object_id_t', 'SAI_LAG_MEMBER_ATTR_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_lag_member_remove(self, npu):

        commands = [{'name': 'lag_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_LAG_MEMBER', 'attributes': ['SAI_LAG_MEMBER_ATTR_LAG_ID', 'sai_object_id_t', 'SAI_LAG_MEMBER_ATTR_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

