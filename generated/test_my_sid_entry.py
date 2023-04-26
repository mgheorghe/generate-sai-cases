

from pprint import pprint

import pytest


class TestSaiMySidEntry:

    @pytest.mark.dependency(scope='session')
    def test_my_sid_entry_create(self, npu):

        commands = [{'name': 'my_sid_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY', 'attributes': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR', 'sai_my_sid_entry_endpoint_behavior_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_my_sid_entry_remove(self, npu):

        commands = [{'name': 'my_sid_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY', 'attributes': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR', 'sai_my_sid_entry_endpoint_behavior_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

