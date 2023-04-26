

from pprint import pprint

import pytest


class TestSaiBridgePort:

    @pytest.mark.dependency(scope='session')
    def test_bridge_port_create(self, npu):

        commands = [{'name': 'bridge_port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT', 'attributes': ['SAI_BRIDGE_PORT_ATTR_TYPE', 'sai_bridge_port_type_t', 'SAI_BRIDGE_PORT_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_BRIDGE_PORT_ATTR_VLAN_ID', '10', 'SAI_BRIDGE_PORT_ATTR_RIF_ID', 'sai_object_id_t', 'SAI_BRIDGE_PORT_ATTR_TUNNEL_ID', 'sai_object_id_t', 'SAI_BRIDGE_PORT_ATTR_BRIDGE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_bridge_port_remove(self, npu):

        commands = [{'name': 'bridge_port_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT', 'attributes': ['SAI_BRIDGE_PORT_ATTR_TYPE', 'sai_bridge_port_type_t', 'SAI_BRIDGE_PORT_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_BRIDGE_PORT_ATTR_VLAN_ID', '10', 'SAI_BRIDGE_PORT_ATTR_RIF_ID', 'sai_object_id_t', 'SAI_BRIDGE_PORT_ATTR_TUNNEL_ID', 'sai_object_id_t', 'SAI_BRIDGE_PORT_ATTR_BRIDGE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

