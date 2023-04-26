

from pprint import pprint

import pytest


class TestSaiBridge:

    @pytest.mark.dependency(scope='session')
    def test_bridge_create(self, npu):

        commands = [{'name': 'bridge_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_BRIDGE', 'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'sai_bridge_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_bridge_remove(self, npu):

        commands = [{'name': 'bridge_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_BRIDGE', 'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'sai_bridge_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

