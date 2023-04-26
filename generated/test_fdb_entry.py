

from pprint import pprint

import pytest


class TestSaiFdbEntry:

    @pytest.mark.dependency(scope='session')
    def test_fdb_entry_create(self, npu):

        commands = [{'name': 'fdb_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_FDB_ENTRY', 'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'sai_fdb_entry_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_fdb_entry_remove(self, npu):

        commands = [{'name': 'fdb_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_FDB_ENTRY', 'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'sai_fdb_entry_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

