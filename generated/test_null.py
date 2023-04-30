from pprint import pprint

import pytest


class TestSaiNull:
    # object with no attributes

    def test_null_create(self, npu):
        commands = [
            {
                'name': 'null_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NULL',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_null_remove(self, npu):
        commands = [
            {
                'name': 'null_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NULL',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
