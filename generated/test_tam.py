

from pprint import pprint

import pytest


class TestSaiTam:

    @pytest.mark.dependency(scope='session')
    def test_tam_create(self, npu):

        commands = [{'name': 'tam_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_remove(self, npu):

        commands = [{'name': 'tam_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

