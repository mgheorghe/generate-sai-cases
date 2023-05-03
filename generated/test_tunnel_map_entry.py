from pprint import pprint


class TestSaiTunnelMapEntry:
    # object with parent SAI_OBJECT_TYPE_TUNNEL_MAP SAI_OBJECT_TYPE_BRIDGE SAI_OBJECT_TYPE_BRIDGE SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_VIRTUAL_ROUTER

    def test_tunnel_map_entry_create(self, npu):
        commands = [
            {
                'name': 'tunnel_map_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP',
                'attributes': [
                    'SAI_TUNNEL_MAP_ATTR_TYPE',
                    'SAI_TUNNEL_MAP_TYPE_OECN_TO_UECN',
                ],
                'key': {'key': 'TODO', 'value': 'TODO'},
            },
            {
                'name': 'bridge_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'virtual_router_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
            {
                'name': 'tunnel_map_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP_ENTRY',
                'attributes': [
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP_TYPE',
                    'SAI_TUNNEL_MAP_TYPE_OECN_TO_UECN',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP',
                    '$tunnel_map_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_KEY',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_VALUE',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_KEY',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_VALUE',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_VALUE',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_VALUE',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_KEY',
                    '$bridge_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_VALUE',
                    '$bridge_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_KEY',
                    '$virtual_router_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_VALUE',
                    '$virtual_router_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_VALUE',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_PREFIX_AGG_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_SRV6_VPN_SID_VALUE',
                    'FF::0',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_tunnel_map_entry_remove(self, npu):
        commands = [
            {
                'name': 'tunnel_map_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP_ENTRY',
                'attributes': [
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP_TYPE',
                    'SAI_TUNNEL_MAP_TYPE_OECN_TO_UECN',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_TUNNEL_MAP',
                    '$tunnel_map_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_KEY',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_OECN_VALUE',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_KEY',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_UECN_VALUE',
                    '1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VLAN_ID_VALUE',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VNI_ID_VALUE',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_KEY',
                    '$bridge_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_BRIDGE_ID_VALUE',
                    '$bridge_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_KEY',
                    '$virtual_router_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VIRTUAL_ROUTER_ID_VALUE',
                    '$virtual_router_1',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_VSID_ID_VALUE',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_PREFIX_AGG_ID_KEY',
                    '10',
                    'SAI_TUNNEL_MAP_ENTRY_ATTR_SRV6_VPN_SID_VALUE',
                    'FF::0',
                ],
            },
            {
                'name': 'virtual_router_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
            {
                'name': 'bridge_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'tunnel_map_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP',
                'attributes': [
                    'SAI_TUNNEL_MAP_ATTR_TYPE',
                    'SAI_TUNNEL_MAP_TYPE_OECN_TO_UECN',
                ],
                'key': {'key': 'TODO', 'value': 'TODO'},
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
