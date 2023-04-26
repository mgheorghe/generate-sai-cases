

from pprint import pprint

import pytest


class TestSaiL:

    @pytest.mark.dependency(scope='session')
    def test_l_create(self, npu):

        commands = [{'name': 'l_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_L', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_l_remove(self, npu):

        commands = [{'name': 'l_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_L', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

