from pprint import pprint

import pytest


class TestSaiL2McEntry:
    # object with no parents

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

    def test_sai_l2mc_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_l2mc_entry_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_L2MC_ENTRY',
                'atrribute': ['SAI_L2MC_ENTRY_ATTR_PACKET_ACTION', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_l2mc_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_l2mc_entry_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_L2MC_ENTRY',
                'atrribute': 'SAI_L2MC_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_l2mc_entry_attr_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_l2mc_entry_attr_output_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_L2MC_ENTRY',
                'atrribute': [
                    'SAI_L2MC_ENTRY_ATTR_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_l2mc_entry_attr_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_l2mc_entry_attr_output_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_L2MC_ENTRY',
                'atrribute': 'SAI_L2MC_ENTRY_ATTR_OUTPUT_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

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
