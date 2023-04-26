

from pprint import pprint

import pytest

# object with no attributes
class TestSaiTamInt:

    @pytest.mark.dependency(scope='session')
    def test_tam_int_create(self, npu):

        commands = [{'name': 'tam_int_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_INT', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_tam_int_remove(self, npu):

        commands = [{'name': 'tam_int_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_INT', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

