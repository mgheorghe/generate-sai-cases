

from pprint import pprint

import pytest

# object with no parents
class TestSaiMySidEntry:

    @pytest.mark.dependency(scope='session')
    def test_my_sid_entry_create(self, npu):

        commands = [{'name': 'my_sid_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY', 'attributes': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR', 'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_E']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_my_sid_entry_remove(self, npu):

        commands = [{'name': 'my_sid_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY', 'attributes': ['SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR', 'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_E']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

