from pprint import pprint

import pytest


class TestSaiDashAclRule:
    # object with parent SAI_OBJECT_TYPE_DASH_ACL_GROUP

    def test_dash_acl_rule_create(self, npu):
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

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_dash_acl_rule_attr_action_set(self, npu):
        commands = [
            {
                'name': 'sai_dash_acl_rule_attr_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': [
                    'SAI_DASH_ACL_RULE_ATTR_ACTION',
                    'SAI_DASH_ACL_RULE_ACTION_PERMIT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dash_acl_rule_attr_action_get(self, npu):
        commands = [
            {
                'name': 'sai_dash_acl_rule_attr_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': 'SAI_DASH_ACL_RULE_ATTR_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_DASH_ACL_RULE_ACTION_PERMIT' for result in results]
        ), 'Get error'

    def test_sai_dash_acl_rule_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'sai_dash_acl_rule_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': [
                    'SAI_DASH_ACL_RULE_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dash_acl_rule_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'sai_dash_acl_rule_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': 'SAI_DASH_ACL_RULE_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_dash_acl_rule_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'sai_dash_acl_rule_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': 'SAI_DASH_ACL_RULE_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_dash_acl_rule_remove(self, npu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'remove',
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
            {
                'name': 'dash_acl_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
