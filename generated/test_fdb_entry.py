

from pprint import pprint

import pytest

# object with no parents
class TestSaiFdbEntry:

    @pytest.mark.dependency(scope='session')
    def test_fdb_entry_create(self, npu):

        commands = [{'name': 'fdb_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_FDB_ENTRY', 'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'SAI_FDB_ENTRY_TYPE_DYNAMIC']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_fdb_entry_remove(self, npu):

        commands = [{'name': 'fdb_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_FDB_ENTRY', 'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'SAI_FDB_ENTRY_TYPE_DYNAMIC']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
