

from pprint import pprint

import pytest

# object with no attributes
class TestSaiHostInterface:

    @pytest.mark.dependency(scope='session')
    def test_host_interface_create(self, npu):

        commands = [{'name': 'host_interface_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HOST_INTERFACE', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_host_interface_remove(self, npu):

        commands = [{'name': 'host_interface_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HOST_INTERFACE', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
