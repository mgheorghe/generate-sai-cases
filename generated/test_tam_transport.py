

from pprint import pprint

import pytest

# object with no attributes
class TestSaiTamTransport:

    @pytest.mark.dependency(scope='session')
    def test_tam_transport_create(self, npu):

        commands = [{'name': 'tam_transport_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_tam_transport_remove(self, npu):

        commands = [{'name': 'tam_transport_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

