

from pprint import pprint

import pytest


class TestSaiInsegEntry:

    @pytest.mark.dependency(scope='session')
    def test_inseg_entry_create(self, npu):

        commands = [{'name': 'inseg_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_inseg_entry_remove(self, npu):

        commands = [{'name': 'inseg_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

