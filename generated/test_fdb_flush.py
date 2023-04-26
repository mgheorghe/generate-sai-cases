

from pprint import pprint

import pytest


class TestSaiFdbFlush:

    @pytest.mark.dependency(scope='session')
    def test_fdb_flush_create(self, npu):

        commands = [{'name': 'fdb_flush_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_FDB_FLUSH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_fdb_flush_remove(self, npu):

        commands = [{'name': 'fdb_flush_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_FDB_FLUSH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
