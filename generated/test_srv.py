

from pprint import pprint

import pytest

# object with no attributes
class TestSaiSrv:

    @pytest.mark.dependency(scope='session')
    def test_srv_create(self, npu):

        commands = [{'name': 'srv_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SRV', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_srv_remove(self, npu):

        commands = [{'name': 'srv_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_SRV', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

