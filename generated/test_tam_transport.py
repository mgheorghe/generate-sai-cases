

from pprint import pprint

import pytest


class TestSaiTamTransport:

    @pytest.mark.dependency(scope='session')
    def test_tam_transport_create(self, npu):

        commands = [{'name': 'tam_transport_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT', 'attributes': ['SAI_TAM_TRANSPORT_ATTR_TRANSPORT_TYPE', 'sai_tam_transport_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_transport_remove(self, npu):

        commands = [{'name': 'tam_transport_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT', 'attributes': ['SAI_TAM_TRANSPORT_ATTR_TRANSPORT_TYPE', 'sai_tam_transport_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
