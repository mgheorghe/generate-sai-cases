from pprint import pprint

import pytest


class TestSaiDashAclGroup:
    # object with no attributes

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

    @pytest.mark.dependency(name='test_sai_dash_acl_group_attr_ip_addr_family_set')
    def test_sai_dash_acl_group_attr_ip_addr_family_set(self, npu):
        commands = [
            {
                'name': 'dash_acl_group_1',
                'op': 'set',
                'attributes': [
                    'SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY',
                    'SAI_IP_ADDR_FAMILY_IPV4',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dash_acl_group_attr_ip_addr_family_set'])
    def test_sai_dash_acl_group_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'dash_acl_group_1',
                'op': 'get',
                'attributes': ['SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_IP_ADDR_FAMILY_IPV4', (
            'Get error, expected SAI_IP_ADDR_FAMILY_IPV4 but got %s' % r_value
        )

    def test_dash_acl_group_remove(self, npu):
        commands = [{'name': 'dash_acl_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
