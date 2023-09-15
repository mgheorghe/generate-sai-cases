from pprint import pprint

import pytest


@pytest.mark.dpu
class TestSaiDashAclRule:
    # object with parent SAI_OBJECT_TYPE_DASH_ACL_GROUP

    def test_dash_acl_rule_create(self, dpu):
        commands = [
            {
                'name': 'dash_acl_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                'attributes': [],
            },
            {
                'name': 'dash_acl_rule_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'attributes': [
                    'SAI_DASH_ACL_RULE_ATTR_DASH_ACL_GROUP_ID',
                    '$dash_acl_group_1',
                    'SAI_DASH_ACL_RULE_ATTR_DIP',
                    'sai_ip_prefix_list_t',
                    'SAI_DASH_ACL_RULE_ATTR_SIP',
                    'sai_ip_prefix_list_t',
                    'SAI_DASH_ACL_RULE_ATTR_PROTOCOL',
                    'sai_u8_list_t',
                    'SAI_DASH_ACL_RULE_ATTR_SRC_PORT',
                    'sai_u16_range_list_t',
                    'SAI_DASH_ACL_RULE_ATTR_DST_PORT',
                    'sai_u16_range_list_t',
                    'SAI_DASH_ACL_RULE_ATTR_PRIORITY',
                    '10',
                ],
            },
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_dash_acl_rule_attr_action_set')
    def test_sai_dash_acl_rule_attr_action_set(self, dpu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'set',
                'attributes': [
                    'SAI_DASH_ACL_RULE_ATTR_ACTION',
                    'SAI_DASH_ACL_RULE_ACTION_PERMIT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_dash_acl_rule_attr_action_set'])
    def test_sai_dash_acl_rule_attr_action_get(self, dpu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'get',
                'attributes': ['SAI_DASH_ACL_RULE_ATTR_ACTION'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_DASH_ACL_RULE_ACTION_PERMIT', (
            'Get error, expected SAI_DASH_ACL_RULE_ACTION_PERMIT but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_dash_acl_rule_attr_counter_id_set')
    def test_sai_dash_acl_rule_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'set',
                'attributes': ['SAI_DASH_ACL_RULE_ATTR_COUNTER_ID', 'null'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_dash_acl_rule_attr_counter_id_set'])
    def test_sai_dash_acl_rule_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'get',
                'attributes': ['SAI_DASH_ACL_RULE_ATTR_COUNTER_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    def test_sai_dash_acl_rule_attr_ip_addr_family_get(self, dpu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'get',
                'attributes': ['SAI_DASH_ACL_RULE_ATTR_IP_ADDR_FAMILY'],
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

    def test_dash_acl_rule_remove(self, dpu):
        commands = [
            {'name': 'dash_acl_rule_1', 'op': 'remove'},
            {'name': 'dash_acl_group_1', 'op': 'remove'},
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
