from pprint import pprint

import pytest


class TestSaiL2McGroup:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_l2mc_group_create(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_l2mc_group_remove(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
