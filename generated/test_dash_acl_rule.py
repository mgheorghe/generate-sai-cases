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

    @pytest.mark.dependency()
    def test_sai_dash_acl_rule_attr_action_set(self, npu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': [
                    'SAI_DASH_ACL_RULE_ATTR_ACTION',
                    'SAI_DASH_ACL_RULE_ACTION_PERMIT',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dash_acl_rule_attr_action_set'])
    def test_sai_dash_acl_rule_attr_action_get(self, npu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': 'SAI_DASH_ACL_RULE_ATTR_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_DASH_ACL_RULE_ACTION_PERMIT', (
            'Get error, expected SAI_DASH_ACL_RULE_ACTION_PERMIT but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dash_acl_rule_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': [
                    'SAI_DASH_ACL_RULE_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dash_acl_rule_attr_counter_id_set'])
    def test_sai_dash_acl_rule_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'dash_acl_rule_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_RULE',
                'atrribute': 'SAI_DASH_ACL_RULE_ATTR_COUNTER_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

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
