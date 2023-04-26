

from pprint import pprint

import pytest


class TestSaiArs:

    @pytest.mark.dependency(scope='session')
    def test_ars_create(self, npu):

        commands = [{'name': 'ars_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ARS', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_ars_remove(self, npu):

        commands = [{'name': 'ars_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_ARS', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

