

from pprint import pprint

import pytest

# object with no attributes
class TestSaiBufferPool:

    @pytest.mark.dependency(scope='session')
    def test_buffer_pool_create(self, npu):

        commands = [{'name': 'buffer_pool_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_BUFFER_POOL', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_buffer_pool_remove(self, npu):

        commands = [{'name': 'buffer_pool_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_BUFFER_POOL', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

