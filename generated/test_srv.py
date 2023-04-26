

from pprint import pprint

import pytest


class TestSaiSrv:

    @pytest.mark.dependency(scope='session')
    def test_srv_create(self, npu):

        commands = [{'name': 'srv_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SRV', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_srv_remove(self, npu):

        commands = [{'name': 'srv_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_SRV', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

