

from pprint import pprint

import pytest


class TestSaiMyMac:

    @pytest.mark.dependency(scope='session')
    def test_my_mac_create(self, npu):

        commands = [{'name': 'my_mac_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MY_MAC', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_my_mac_remove(self, npu):

        commands = [{'name': 'my_mac_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MY_MAC', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

