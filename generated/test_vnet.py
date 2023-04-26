

from pprint import pprint

import pytest


class TestSaiVnet:

    @pytest.mark.dependency(scope='session')
    def test_vnet_create(self, npu):

        commands = [{'name': 'vnet_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_VNET', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_vnet_remove(self, npu):

        commands = [{'name': 'vnet_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_VNET', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

