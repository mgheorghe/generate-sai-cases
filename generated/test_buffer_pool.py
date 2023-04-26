

from pprint import pprint

import pytest

# object with no parents
class TestSaiBufferPool:

    @pytest.mark.dependency(scope='session')
    def test_buffer_pool_create(self, npu):

        commands = [{'name': 'buffer_pool_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_BUFFER_POOL', 'attributes': ['SAI_BUFFER_POOL_ATTR_TYPE', 'sai_buffer_pool_type_t', 'SAI_BUFFER_POOL_ATTR_SIZE', 'sai_uint64_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_buffer_pool_remove(self, npu):

        commands = [{'name': 'buffer_pool_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_BUFFER_POOL', 'attributes': ['SAI_BUFFER_POOL_ATTR_TYPE', 'sai_buffer_pool_type_t', 'SAI_BUFFER_POOL_ATTR_SIZE', 'sai_uint64_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

