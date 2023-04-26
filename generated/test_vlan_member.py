

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_VLAN SAI_OBJECT_TYPE_BRIDGE_PORT
class TestSaiVlanMember:

    @pytest.mark.dependency(scope='session')
    def test_vlan_member_create(self, npu):

        commands = [{'name': 'vlan_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_VLAN_MEMBER', 'attributes': ['SAI_VLAN_MEMBER_ATTR_VLAN_ID', 'sai_object_id_t', 'SAI_VLAN_MEMBER_ATTR_BRIDGE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_vlan_member_remove(self, npu):

        commands = [{'name': 'vlan_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_VLAN_MEMBER', 'attributes': ['SAI_VLAN_MEMBER_ATTR_VLAN_ID', 'sai_object_id_t', 'SAI_VLAN_MEMBER_ATTR_BRIDGE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

