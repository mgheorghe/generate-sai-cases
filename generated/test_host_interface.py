

from pprint import pprint

import pytest


class TestSaiHostInterface:

    @pytest.mark.dependency(scope='session')
    def test_host_interface_create(self, npu):

        commands = [{'name': 'host_interface_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HOST_INTERFACE', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_host_interface_remove(self, npu):

        commands = [{'name': 'host_interface_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HOST_INTERFACE', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
