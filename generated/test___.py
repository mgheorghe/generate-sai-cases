from pprint import pprint

import pytest


class TestSai:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test____create(self, npu):
        commands = [
            {
                'name': '___1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE___',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test____remove(self, npu):
        commands = [
            {
                'name': '___1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE___',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
