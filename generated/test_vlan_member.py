from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiVlanMember:
    # object with parent SAI_OBJECT_TYPE_VLAN SAI_OBJECT_TYPE_BRIDGE_PORT

    def test_vlan_member_create(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
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
                'name': 'virtual_router_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
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
                'name': 'bridge_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'attributes': [
                    'SAI_BRIDGE_PORT_ATTR_TYPE',
                    'SAI_BRIDGE_PORT_TYPE_PORT',
                    'SAI_BRIDGE_PORT_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_BRIDGE_PORT_ATTR_VLAN_ID',
                    '10',
                    'SAI_BRIDGE_PORT_ATTR_RIF_ID',
                    '$router_interface_1',
                    'SAI_BRIDGE_PORT_ATTR_TUNNEL_ID',
                    '$tunnel_1',
                    'SAI_BRIDGE_PORT_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'vlan_member_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN_MEMBER',
                'attributes': [
                    'SAI_VLAN_MEMBER_ATTR_VLAN_ID',
                    '$vlan_1',
                    'SAI_VLAN_MEMBER_ATTR_BRIDGE_PORT_ID',
                    '$bridge_port_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_vlan_member_attr_vlan_tagging_mode_set')
    def test_sai_vlan_member_attr_vlan_tagging_mode_set(self, npu):
        commands = [
            {
                'name': 'vlan_member_1',
                'op': 'set',
                'attributes': [
                    'SAI_VLAN_MEMBER_ATTR_VLAN_TAGGING_MODE',
                    'SAI_VLAN_TAGGING_MODE_UNTAGGED',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_vlan_member_attr_vlan_tagging_mode_set'])
    def test_sai_vlan_member_attr_vlan_tagging_mode_get(self, npu):
        commands = [
            {
                'name': 'vlan_member_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_MEMBER_ATTR_VLAN_TAGGING_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_VLAN_TAGGING_MODE_UNTAGGED', (
            'Get error, expected SAI_VLAN_TAGGING_MODE_UNTAGGED but got %s' % r_value
        )

    def test_vlan_member_remove(self, npu):
        commands = [
            {'name': 'vlan_member_1', 'op': 'remove'},
            {'name': 'bridge_port_1', 'op': 'remove'},
            {'name': 'tunnel_1', 'op': 'remove'},
            {'name': 'router_interface_1', 'op': 'remove'},
            {'name': 'bridge_1', 'op': 'remove'},
            {'name': 'virtual_router_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
            {'name': 'vlan_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
