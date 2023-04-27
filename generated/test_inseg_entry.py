from pprint import pprint

import pytest


class TestSaiInsegEntry:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_inseg_entry_create(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_inseg_entry_remove(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
