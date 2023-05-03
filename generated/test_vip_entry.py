from pprint import pprint

import pytest


class TestSaiVipEntry:
    # object with no attributes

    def test_vip_entry_create(self, npu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vip': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_vip_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'atrribute': [
                    'SAI_VIP_ENTRY_ATTR_ACTION',
                    'SAI_VIP_ENTRY_ACTION_ACCEPT',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vip_entry_attr_action_set'])
    def test_sai_vip_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'atrribute': 'SAI_VIP_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_VIP_ENTRY_ACTION_ACCEPT', (
            'Get error, expected SAI_VIP_ENTRY_ACTION_ACCEPT but got %s'
            % results[1][0].value()
        )

    def test_vip_entry_remove(self, npu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vip': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
