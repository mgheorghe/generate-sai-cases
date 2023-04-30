from pprint import pprint

import pytest


class TestSaiExtensionsRangeStart:
    # object with no attributes

    def test_extensions_range_start_create(self, npu):
        commands = [
            {
                'name': 'extensions_range_start_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_START',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_extensions_range_start_remove(self, npu):
        commands = [
            {
                'name': 'extensions_range_start_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_START',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
