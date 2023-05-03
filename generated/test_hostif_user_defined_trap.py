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

    @pytest.mark.dependency()
    def test_sai_hostif_user_defined_trap_attr_trap_priority_set(self, npu):
        commands = [
            {
                'name': 'hostif_user_defined_trap_1',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_hostif_user_defined_trap_attr_trap_priority_set']
    )
    def test_sai_hostif_user_defined_trap_attr_trap_priority_get(self, npu):
        commands = [
            {
                'name': 'hostif_user_defined_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'atrribute': 'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TRAP_PRIORITY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[1][0].value()
            == 'attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY'
        ), (
            'Get error, expected attrvalue SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_hostif_user_defined_trap_attr_trap_group_set(self, npu):
        commands = [
            {
                'name': 'hostif_user_defined_trap_1',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_hostif_user_defined_trap_attr_trap_group_set']
    )
    def test_sai_hostif_user_defined_trap_attr_trap_group_get(self, npu):
        commands = [
            {
                'name': 'hostif_user_defined_trap_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP',
                'atrribute': 'SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TRAP_GROUP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[1][0].value() == 'attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP'
        ), (
            'Get error, expected attrvalue SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP but got %s'
            % results[1][0].value()
        )

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
