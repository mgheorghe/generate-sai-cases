

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_PORT, SAI_OBJECT_TYPE_LAG, SAI_OBJECT_TYPE_SYSTEM_PORT SAI_OBJECT_TYPE_VLAN SAI_OBJECT_TYPE_BRIDGE
class TestSaiRouterInterface:

    @pytest.mark.dependency(scope='session')
    def test_router_interface_create(self, npu):

        commands = [{'name': 'router_interface_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE', 'attributes': ['SAI_ROUTER_INTERFACE_ATTR_VIRTUAL_ROUTER_ID', 'sai_object_id_t', 'SAI_ROUTER_INTERFACE_ATTR_TYPE', 'sai_router_interface_type_t', 'SAI_ROUTER_INTERFACE_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_ROUTER_INTERFACE_ATTR_VLAN_ID', 'sai_object_id_t', 'SAI_ROUTER_INTERFACE_ATTR_OUTER_VLAN_ID', '10', 'SAI_ROUTER_INTERFACE_ATTR_INNER_VLAN_ID', '10', 'SAI_ROUTER_INTERFACE_ATTR_BRIDGE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_router_interface_remove(self, npu):

        commands = [{'name': 'router_interface_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE', 'attributes': ['SAI_ROUTER_INTERFACE_ATTR_VIRTUAL_ROUTER_ID', 'sai_object_id_t', 'SAI_ROUTER_INTERFACE_ATTR_TYPE', 'sai_router_interface_type_t', 'SAI_ROUTER_INTERFACE_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_ROUTER_INTERFACE_ATTR_VLAN_ID', 'sai_object_id_t', 'SAI_ROUTER_INTERFACE_ATTR_OUTER_VLAN_ID', '10', 'SAI_ROUTER_INTERFACE_ATTR_INNER_VLAN_ID', '10', 'SAI_ROUTER_INTERFACE_ATTR_BRIDGE_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
