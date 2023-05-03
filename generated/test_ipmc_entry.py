from pprint import pprint

import pytest


class TestSaiIpmcEntry:
    # object with parent SAI_OBJECT_TYPE_RPF_GROUP

    def test_ipmc_entry_create(self, npu):
        commands = [
            {
                'name': 'rpf_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_RPF_GROUP',
                'attributes': [],
            },
            {
                'name': 'ipmc_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'attributes': [
                    'SAI_IPMC_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                    'SAI_IPMC_ENTRY_ATTR_RPF_GROUP_ID',
                    '$rpf_group_1',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'type': 'TODO',
                    'destination': 'TODO',
                    'source': 'TODO',
                },
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_ipmc_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': ['SAI_IPMC_ENTRY_ATTR_PACKET_ACTION', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipmc_entry_attr_packet_action_set'])
    def test_sai_ipmc_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': 'SAI_IPMC_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipmc_entry_attr_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': [
                    'SAI_IPMC_ENTRY_ATTR_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipmc_entry_attr_output_group_id_set'])
    def test_sai_ipmc_entry_attr_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': 'SAI_IPMC_ENTRY_ATTR_OUTPUT_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipmc_entry_attr_rpf_group_id_set(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': ['SAI_IPMC_ENTRY_ATTR_RPF_GROUP_ID', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipmc_entry_attr_rpf_group_id_set'])
    def test_sai_ipmc_entry_attr_rpf_group_id_get(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': 'SAI_IPMC_ENTRY_ATTR_RPF_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipmc_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': ['SAI_IPMC_ENTRY_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipmc_entry_attr_counter_id_set'])
    def test_sai_ipmc_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'atrribute': 'SAI_IPMC_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_ipmc_entry_remove(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'attributes': [
                    'SAI_IPMC_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                    'SAI_IPMC_ENTRY_ATTR_RPF_GROUP_ID',
                    '$rpf_group_1',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'type': 'TODO',
                    'destination': 'TODO',
                    'source': 'TODO',
                },
            },
            {
                'name': 'rpf_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_RPF_GROUP',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
