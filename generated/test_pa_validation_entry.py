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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_pa_validation_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'sai_pa_validation_entry_attr_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'atrribute': [
                    'SAI_PA_VALIDATION_ENTRY_ATTR_ACTION',
                    'SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_pa_validation_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'sai_pa_validation_entry_attr_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'atrribute': 'SAI_PA_VALIDATION_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT' for result in results]
        ), 'Get error'

    def test_sai_pa_validation_entry_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'sai_pa_validation_entry_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'atrribute': 'SAI_PA_VALIDATION_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_pa_validation_entry_remove(self, npu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
