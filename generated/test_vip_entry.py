from pprint import pprint

import pytest


@pytest.mark.dpu
class TestSaiVipEntry:
    # object with no attributes

    def test_vip_entry_create(self, dpu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vip': 'TODO'},
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_vip_entry_attr_action_set')
    def test_sai_vip_entry_attr_action_set(self, dpu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_VIP_ENTRY_ATTR_ACTION',
                    'SAI_VIP_ENTRY_ACTION_ACCEPT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_vip_entry_attr_action_set'])
    def test_sai_vip_entry_attr_action_get(self, dpu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'get',
                'attributes': ['SAI_VIP_ENTRY_ATTR_ACTION'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_VIP_ENTRY_ACTION_ACCEPT', (
            'Get error, expected SAI_VIP_ENTRY_ACTION_ACCEPT but got %s' % r_value
        )

    def test_sai_vip_entry_attr_ip_addr_family_get(self, dpu):
        commands = [
            {
                'name': 'vip_entry_1',
                'op': 'get',
                'attributes': ['SAI_VIP_ENTRY_ATTR_IP_ADDR_FAMILY'],
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

    def test_vip_entry_remove(self, dpu):
        commands = [
            {
                'name': 'vip_entry_1',
                'key': {'switch_id': '$SWITCH_ID', 'vip': 'TODO'},
                'op': 'remove',
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
