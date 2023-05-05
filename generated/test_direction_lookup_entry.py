from pprint import pprint

import pytest


class TestSaiDirectionLookupEntry:
    # object with no attributes

    def test_direction_lookup_entry_create(self, npu):
        commands = [
            {
                'name': 'direction_lookup_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vni': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_direction_lookup_entry_attr_action_set')
    def test_sai_direction_lookup_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'direction_lookup_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION',
                    'SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_direction_lookup_entry_attr_action_set'])
    def test_sai_direction_lookup_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'direction_lookup_entry_1',
                'op': 'get',
                'attributes': ['SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION', (
            'Get error, expected SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION but got %s'
            % r_value
        )

    def test_direction_lookup_entry_remove(self, npu):
        commands = [
            {
                'name': 'direction_lookup_entry_1',
                'key': {'switch_id': '$SWITCH_ID', 'vni': 'TODO'},
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
