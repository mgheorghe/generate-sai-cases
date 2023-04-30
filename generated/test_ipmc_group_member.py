from pprint import pprint

import pytest


class TestSaiIpmcGroupMember:
    # object with parent SAI_OBJECT_TYPE_IPMC_GROUP SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_TUNNEL

    def test_ipmc_group_member_create(self, npu):
        commands = [
            {
                'name': 'ipmc_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP',
                'attributes': [],
            },
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
                'name': 'ipmc_group_member_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP_MEMBER',
                'attributes': [
                    'SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_GROUP_ID',
                    '$ipmc_group_1',
                    'SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_OUTPUT_ID',
                    '$router_interface_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_ipmc_group_member_remove(self, npu):
        commands = [
            {
                'name': 'ipmc_group_member_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP_MEMBER',
                'attributes': [
                    'SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_GROUP_ID',
                    '$ipmc_group_1',
                    'SAI_IPMC_GROUP_MEMBER_ATTR_IPMC_OUTPUT_ID',
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
            {
                'name': 'ipmc_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
