from pprint import pprint

import pytest


class TestSaiVipEntry:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_vip_entry_create(self, npu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_vip_entry_attr_action_set(self, dpu):
        commands = [
            {
                'name': 'sai_vip_entry_attr_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'atrribute': [
                    'SAI_VIP_ENTRY_ATTR_ACTION',
                    'SAI_VIP_ENTRY_ACTION_ACCEPT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vip_entry_attr_action_get(self, dpu):
        commands = [
            {
                'name': 'sai_vip_entry_attr_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'atrribute': 'SAI_VIP_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_VIP_ENTRY_ACTION_ACCEPT' for result in results]
        ), 'Get error'

    def test_sai_vip_entry_attr_ip_addr_family_get(self, dpu):
        commands = [
            {
                'name': 'sai_vip_entry_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'atrribute': 'SAI_VIP_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_vip_entry_remove(self, npu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
