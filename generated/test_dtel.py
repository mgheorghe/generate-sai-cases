

from pprint import pprint

import pytest

# object with no attributes
class TestSaiDtel:

    @pytest.mark.dependency(scope='session')
    def test_dtel_create(self, npu):

        commands = [{'name': 'dtel_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DTEL', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_dtel_remove(self, npu):

        commands = [{'name': 'dtel_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DTEL', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
