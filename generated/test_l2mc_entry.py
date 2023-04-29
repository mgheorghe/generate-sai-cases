from pprint import pprint

import pytest


class TestSaiL2McEntry:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_l2mc_entry_create(self, npu):
        commands = [
            {
                'name': 'l2mc_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_L2MC_ENTRY',
                'attributes': [
                    'SAI_L2MC_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_l2mc_entry_remove(self, npu):
        commands = [
            {
                'name': 'l2mc_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_L2MC_ENTRY',
                'attributes': [
                    'SAI_L2MC_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
