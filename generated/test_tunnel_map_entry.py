

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_TUNNEL_MAP SAI_OBJECT_TYPE_BRIDGE SAI_OBJECT_TYPE_BRIDGE SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_VIRTUAL_ROUTER
class TestSaiTunnelMapEntry:

    @pytest.mark.dependency(scope='session')
    def test_tunnel_map_entry_create(self, npu):

        commands = [{'name': 'tunnel_map_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP_ENTRY', 'attributes': ['SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP_TYPE', 'sai_tunnel_map_type_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_KEY', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_VALUE', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_KEY', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_VALUE', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_KEY', '10', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_VALUE', '10', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_KEY', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_VALUE', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_KEY', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_VALUE', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_KEY', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_VALUE', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_KEY', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_VALUE', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_PREFIX_AGG_ID_KEY', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_SRV6_VPN_SID_VALUE', 'sai_ip6_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_tunnel_map_entry_remove(self, npu):

        commands = [{'name': 'tunnel_map_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP_ENTRY', 'attributes': ['SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP_TYPE', 'sai_tunnel_map_type_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_KEY', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_VALUE', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_KEY', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_VALUE', 'sai_uint8_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_KEY', '10', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_VALUE', '10', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_KEY', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_VALUE', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_KEY', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_VALUE', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_KEY', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_VALUE', 'sai_object_id_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_KEY', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_VALUE', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_PREFIX_AGG_ID_KEY', 'sai_uint32_t', 'SAI_TUNNEL_MAP_ENTRY_ATTR_SRV6_VPN_SID_VALUE', 'sai_ip6_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

