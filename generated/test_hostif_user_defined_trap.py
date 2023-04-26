

from pprint import pprint

import pytest


class TestSaiHostifUserDefinedTrap:

    @pytest.mark.dependency(scope='session')
    def test_hostif_user_defined_trap_create(self, npu):

        commands = [{'name': 'hostif_user_defined_trap_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP', 'attributes': ['SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TYPE', 'sai_hostif_user_defined_trap_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_hostif_user_defined_trap_remove(self, npu):

        commands = [{'name': 'hostif_user_defined_trap_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP', 'attributes': ['SAI_HOSTIF_USER_DEFINED_TRAP_ATTR_TYPE', 'sai_hostif_user_defined_trap_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
