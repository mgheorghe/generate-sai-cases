

from pprint import pprint

import pytest


class TestSaiPaValidationEntry:

    @pytest.mark.dependency(scope='session')
    def test_pa_validation_entry_create(self, npu):

        commands = [{'name': 'pa_validation_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_pa_validation_entry_remove(self, npu):

        commands = [{'name': 'pa_validation_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

