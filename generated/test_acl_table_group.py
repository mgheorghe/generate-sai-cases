from pprint import pprint

import pytest


class TestSaiAclTableGroup:
    # object with no parents

    def test_acl_table_group_create(self, npu):
        commands = [
            {
                'name': 'acl_table_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP',
                'attributes': [
                    'SAI_ACL_TABLE_GROUP_ATTR_ACL_STAGE',
                    'SAI_ACL_STAGE_INGRESS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_acl_table_group_attr_member_list_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_table_group_attr_member_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP',
                'atrribute': 'SAI_ACL_TABLE_GROUP_ATTR_MEMBER_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_acl_table_group_remove(self, npu):
        commands = [
            {
                'name': 'acl_table_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE_GROUP',
                'attributes': [
                    'SAI_ACL_TABLE_GROUP_ATTR_ACL_STAGE',
                    'SAI_ACL_STAGE_INGRESS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
