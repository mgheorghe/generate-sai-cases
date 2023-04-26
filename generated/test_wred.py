

from pprint import pprint

import pytest


class TestSaiWred:

    @pytest.mark.dependency(scope='session')
    def test_wred_create(self, npu):

        commands = [{'name': 'wred_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_WRED', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_wred_remove(self, npu):

        commands = [{'name': 'wred_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_WRED', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
