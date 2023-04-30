from pprint import pprint

import pytest


class TestSaiHostifUserDefinedTrap:
    # object with no parents

    def test_hostif_user_defined_trap_create(self, npu):
        commands = [
            {
                'name': 'hostif_user_defined_trap_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'attributes': [
                    'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TYPE',
                    'SAI_HOSTIF_USER_DEFINED_TRAP_TYPE_END',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_hostif_user_defined_trap_attr_trap_priority_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_user_defined_trap_attr_trap_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'atrribute': [
                    'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TRAP_PRIORITY',
                    'attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_user_defined_trap_attr_trap_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_user_defined_trap_attr_trap_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'atrribute': 'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TRAP_PRIORITY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY'
                for result in results
            ]
        ), 'Get error'

    def test_sai_hostif_user_defined_trap_attr_trap_group_set(self, npu):
        commands = [
            {
                'name': 'sai_hostif_user_defined_trap_attr_trap_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'atrribute': [
                    'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TRAP_GROUP',
                    'attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hostif_user_defined_trap_attr_trap_group_get(self, npu):
        commands = [
            {
                'name': 'sai_hostif_user_defined_trap_attr_trap_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'atrribute': 'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TRAP_GROUP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP'
                for result in results
            ]
        ), 'Get error'

    def test_hostif_user_defined_trap_remove(self, npu):
        commands = [
            {
                'name': 'hostif_user_defined_trap_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'attributes': [
                    'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TYPE',
                    'SAI_HOSTIF_USER_DEFINED_TRAP_TYPE_END',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
