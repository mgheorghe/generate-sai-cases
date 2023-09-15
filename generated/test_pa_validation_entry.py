from pprint import pprint

import pytest


@pytest.mark.dpu
class TestSaiPaValidationEntry:
    # object with no attributes

    def test_pa_validation_entry_create(self, dpu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vnet_id': 'TODO', 'sip': 'TODO'},
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_pa_validation_entry_attr_action_set')
    def test_sai_pa_validation_entry_attr_action_set(self, dpu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_PA_VALIDATION_ENTRY_ATTR_ACTION',
                    'SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_pa_validation_entry_attr_action_set'])
    def test_sai_pa_validation_entry_attr_action_get(self, dpu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'get',
                'attributes': ['SAI_PA_VALIDATION_ENTRY_ATTR_ACTION'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT', (
            'Get error, expected SAI_PA_VALIDATION_ENTRY_ACTION_PERMIT but got %s'
            % r_value
        )

    def test_sai_pa_validation_entry_attr_ip_addr_family_get(self, dpu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'get',
                'attributes': ['SAI_PA_VALIDATION_ENTRY_ATTR_IP_ADDR_FAMILY'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_pa_validation_entry_remove(self, dpu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'key': {'switch_id': '$SWITCH_ID', 'vnet_id': 'TODO', 'sip': 'TODO'},
                'op': 'remove',
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
