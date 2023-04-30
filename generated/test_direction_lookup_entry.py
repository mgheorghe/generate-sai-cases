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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_direction_lookup_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'sai_direction_lookup_entry_attr_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY',
                'atrribute': [
                    'SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION',
                    'SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_direction_lookup_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'sai_direction_lookup_entry_attr_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY',
                'atrribute': 'SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION'
                for result in results
            ]
        ), 'Get error'

    def test_direction_lookup_entry_remove(self, npu):
        commands = [
            {
                'name': 'direction_lookup_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
