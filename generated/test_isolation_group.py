from pprint import pprint

import pytest


class TestSaiIsolationGroup:
    # object with no parents

    def test_isolation_group_create(self, npu):
        commands = [
            {
                'name': 'isolation_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP',
                'attributes': [
                    'SAI_ISOLATION_GROUP_ATTR_TYPE',
                    'SAI_ISOLATION_GROUP_TYPE_PORT',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_isolation_group_attr_isolation_member_list_get(self, npu):
        commands = [
            {
                'name': 'sai_isolation_group_attr_isolation_member_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP',
                'atrribute': 'SAI_ISOLATION_GROUP_ATTR_ISOLATION_MEMBER_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_isolation_group_remove(self, npu):
        commands = [
            {
                'name': 'isolation_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP',
                'attributes': [
                    'SAI_ISOLATION_GROUP_ATTR_TYPE',
                    'SAI_ISOLATION_GROUP_TYPE_PORT',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
