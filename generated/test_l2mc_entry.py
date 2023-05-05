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
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'bv_id': 'TODO',
                    'type': 'TODO',
                    'destination': 'TODO',
                    'source': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_l2mc_entry_attr_packet_action_set')
    def test_sai_l2mc_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'l2mc_entry_1',
                'op': 'set',
                'attributes': ['SAI_L2MC_ENTRY_ATTR_PACKET_ACTION', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_l2mc_entry_attr_packet_action_set'])
    def test_sai_l2mc_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'l2mc_entry_1',
                'op': 'get',
                'attributes': ['SAI_L2MC_ENTRY_ATTR_PACKET_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_l2mc_entry_attr_output_group_id_set')
    def test_sai_l2mc_entry_attr_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'l2mc_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_L2MC_ENTRY_ATTR_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_l2mc_entry_attr_output_group_id_set'])
    def test_sai_l2mc_entry_attr_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'l2mc_entry_1',
                'op': 'get',
                'attributes': ['SAI_L2MC_ENTRY_ATTR_OUTPUT_GROUP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    def test_l2mc_entry_remove(self, npu):
        commands = [
            {
                'name': 'l2mc_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'bv_id': 'TODO',
                    'type': 'TODO',
                    'destination': 'TODO',
                    'source': 'TODO',
                },
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
