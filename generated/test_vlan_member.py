

from pprint import pprint

import pytest


class TestSaiVlanMember:

    @pytest.mark.dependency(scope='session')
    def test_vlan_member_create(self, npu):

        commands = [{'name': 'vlan_member_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_VLAN_MEMBER', 'attributes': ['SAI_VLAN_MEMBER_ATTR_VLAN_ID', 'sai_object_id_t', 'SAI_VLAN_MEMBER_ATTR_BRIDGE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_vlan_member_remove(self, npu):

        commands = [{'name': 'vlan_member_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_VLAN_MEMBER', 'attributes': ['SAI_VLAN_MEMBER_ATTR_VLAN_ID', 'sai_object_id_t', 'SAI_VLAN_MEMBER_ATTR_BRIDGE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

