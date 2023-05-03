from pprint import pprint

import pytest


class TestSaiPaValidationEntry:
    # object with no attributes

    def test_pa_validation_entry_create(self, npu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vnet_id': 'TODO', 'sip': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_pa_validation_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'atrribute': [
                    'SAI_PA_VALIDATION_ENTRY_ATTR_ACTION',
                    'SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_pa_validation_entry_attr_action_set'])
    def test_sai_pa_validation_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'atrribute': 'SAI_PA_VALIDATION_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT', (
            'Get error, expected SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT but got %s'
            % results[1][0].value()
        )

    def test_pa_validation_entry_remove(self, npu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vnet_id': 'TODO', 'sip': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
