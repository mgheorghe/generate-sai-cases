from pprint import pprint

import pytest


class TestSaiTableBitmapRouterEntry:
    # object with parent SAI_OBJECT_TYPE_NEXT_HOP SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_HOSTIF_TRAP

    @pytest.mark.dependency(scope='session')
    def test_table_bitmap_router_entry_create(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'vlan_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            },
            {
                'name': 'bridge_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'router_interface_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'attributes': [
                    'SAI_ROUTER_INTERFACE_ATTR_VIRTUAL_ROUTER_ID',
                    '$virtual_router_1',
                    'SAI_ROUTER_INTERFACE_ATTR_TYPE',
                    'SAI_ROUTER_INTERFACE_TYPE_PORT',
                    'SAI_ROUTER_INTERFACE_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_ROUTER_INTERFACE_ATTR_VLAN_ID',
                    '$vlan_1',
                    'SAI_ROUTER_INTERFACE_ATTR_OUTER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_INNER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'tunnel_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'attributes': [
                    'SAI_TUNNEL_ATTR_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE',
                    '$router_interface_1',
                    'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE',
                    '$router_interface_1',
                ],
            },
            {
                'name': 'srv6_sidlist_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            },
            {
                'name': 'next_hop_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'attributes': [
                    'SAI_NEXT_HOP_ATTR_TYPE',
                    'SAI_NEXT_HOP_TYPE_IP',
                    'SAI_NEXT_HOP_ATTR_IP',
                    'sai_ip_address_t',
                    'SAI_NEXT_HOP_ATTR_ROUTER_INTERFACE_ID',
                    '$router_interface_1',
                    'SAI_NEXT_HOP_ATTR_TUNNEL_ID',
                    '$tunnel_1',
                    'SAI_NEXT_HOP_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                    'SAI_NEXT_HOP_ATTR_LABELSTACK',
                    '2:10,11',
                ],
            },
            {
                'name': 'hostif_trap_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'SAI_HOSTIF_TRAP_TYPE_STP',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            },
            {
                'name': 'table_bitmap_router_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TABLE_BITMAP_ROUTER_ENTRY',
                'attributes': [
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ACTION',
                    'sai_table_bitmap_router_entry_action_t',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_PRIORITY',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_KEY',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_MASK',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_DST_IP_KEY',
                    'sai_ip_prefix_t',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TUNNEL_INDEX',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_NEXT_HOP',
                    '$next_hop_1',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ROUTER_INTERFACE',
                    '$router_interface_1',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TRAP_ID',
                    '$hostif_trap_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_table_bitmap_router_entry_remove(self, npu):
        commands = [
            {
                'name': 'table_bitmap_router_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TABLE_BITMAP_ROUTER_ENTRY',
                'attributes': [
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ACTION',
                    'sai_table_bitmap_router_entry_action_t',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_PRIORITY',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_KEY',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_MASK',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_DST_IP_KEY',
                    'sai_ip_prefix_t',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TUNNEL_INDEX',
                    '10',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_NEXT_HOP',
                    '$next_hop_1',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ROUTER_INTERFACE',
                    '$router_interface_1',
                    'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TRAP_ID',
                    '$hostif_trap_1',
                ],
            },
            {
                'name': 'hostif_trap_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'SAI_HOSTIF_TRAP_TYPE_STP',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            },
            {
                'name': 'next_hop_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP',
                'attributes': [
                    'SAI_NEXT_HOP_ATTR_TYPE',
                    'SAI_NEXT_HOP_TYPE_IP',
                    'SAI_NEXT_HOP_ATTR_IP',
                    'sai_ip_address_t',
                    'SAI_NEXT_HOP_ATTR_ROUTER_INTERFACE_ID',
                    '$router_interface_1',
                    'SAI_NEXT_HOP_ATTR_TUNNEL_ID',
                    '$tunnel_1',
                    'SAI_NEXT_HOP_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                    'SAI_NEXT_HOP_ATTR_LABELSTACK',
                    '2:10,11',
                ],
            },
            {
                'name': 'srv6_sidlist_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            },
            {
                'name': 'tunnel_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'attributes': [
                    'SAI_TUNNEL_ATTR_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE',
                    '$router_interface_1',
                    'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE',
                    '$router_interface_1',
                ],
            },
            {
                'name': 'router_interface_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'attributes': [
                    'SAI_ROUTER_INTERFACE_ATTR_VIRTUAL_ROUTER_ID',
                    '$virtual_router_1',
                    'SAI_ROUTER_INTERFACE_ATTR_TYPE',
                    'SAI_ROUTER_INTERFACE_TYPE_PORT',
                    'SAI_ROUTER_INTERFACE_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_ROUTER_INTERFACE_ATTR_VLAN_ID',
                    '$vlan_1',
                    'SAI_ROUTER_INTERFACE_ATTR_OUTER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_INNER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'bridge_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'vlan_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'virtual_router_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
