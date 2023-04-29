from pprint import pprint

import pytest


class TestSaiDashAclGroup:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_dash_acl_group_create(self, npu):
        commands = [
            {
                'name': 'dash_acl_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_dash_acl_group_attr_ip_addr_family_set(self, dpu):
        commands = [
            {
                'name': 'sai_dash_acl_group_attr_ip_addr_family_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                'atrribute': [
                    'SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY',
                    'SAI_IP_ADDR_FAMILY_IPV4',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dash_acl_group_attr_ip_addr_family_get(self, dpu):
        commands = [
            {
                'name': 'sai_dash_acl_group_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                'atrribute': 'SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_IP_ADDR_FAMILY_IPV4' for result in results]
        ), 'Get error'

    def test_dash_acl_group_remove(self, npu):
        commands = [
            {
                'name': 'dash_acl_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DASH_ACL_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
