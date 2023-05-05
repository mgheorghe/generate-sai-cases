from pprint import pprint

import pytest


class TestSaiRouterInterface:
    # object with parent SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT SAI_OBJECT_TYPE_VLAN SAI_OBJECT_TYPE_BRIDGE

    def test_router_interface_create(self, npu):
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
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_src_mac_address_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': [
                    'SAI_ROUTER_INTERFACE_ATTR_SRC_MAC_ADDRESS',
                    'attrvalue SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_src_mac_address_set']
    )
    def test_sai_router_interface_attr_src_mac_address_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_SRC_MAC_ADDRESS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[0][0].value() == 'attrvalue SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS'
        ), (
            'Get error, expected attrvalue SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_admin_v4_state_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': ['SAI_ROUTER_INTERFACE_ATTR_ADMIN_V4_STATE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_admin_v4_state_set']
    )
    def test_sai_router_interface_attr_admin_v4_state_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_ADMIN_V4_STATE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'true', (
            'Get error, expected true but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_admin_v6_state_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': ['SAI_ROUTER_INTERFACE_ATTR_ADMIN_V6_STATE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_admin_v6_state_set']
    )
    def test_sai_router_interface_attr_admin_v6_state_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_ADMIN_V6_STATE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'true', (
            'Get error, expected true but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_mtu_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': ['SAI_ROUTER_INTERFACE_ATTR_MTU', '1514'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_router_interface_attr_mtu_set'])
    def test_sai_router_interface_attr_mtu_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_MTU'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '1514', (
            'Get error, expected 1514 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': [
                    'SAI_ROUTER_INTERFACE_ATTR_INGRESS_ACL',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_router_interface_attr_ingress_acl_set'])
    def test_sai_router_interface_attr_ingress_acl_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_INGRESS_ACL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_egress_acl_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': [
                    'SAI_ROUTER_INTERFACE_ATTR_EGRESS_ACL',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_router_interface_attr_egress_acl_set'])
    def test_sai_router_interface_attr_egress_acl_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_EGRESS_ACL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_neighbor_miss_packet_action_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': [
                    'SAI_ROUTER_INTERFACE_ATTR_NEIGHBOR_MISS_PACKET_ACTION',
                    'SAI_PACKET_ACTION_TRAP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_neighbor_miss_packet_action_set']
    )
    def test_sai_router_interface_attr_neighbor_miss_packet_action_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_NEIGHBOR_MISS_PACKET_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_PACKET_ACTION_TRAP', (
            'Get error, expected SAI_PACKET_ACTION_TRAP but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_v4_mcast_enable_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': ['SAI_ROUTER_INTERFACE_ATTR_V4_MCAST_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_v4_mcast_enable_set']
    )
    def test_sai_router_interface_attr_v4_mcast_enable_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_V4_MCAST_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_v6_mcast_enable_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': ['SAI_ROUTER_INTERFACE_ATTR_V6_MCAST_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_v6_mcast_enable_set']
    )
    def test_sai_router_interface_attr_v6_mcast_enable_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_V6_MCAST_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_loopback_packet_action_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': [
                    'SAI_ROUTER_INTERFACE_ATTR_LOOPBACK_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_loopback_packet_action_set']
    )
    def test_sai_router_interface_attr_loopback_packet_action_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_LOOPBACK_PACKET_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_PACKET_ACTION_FORWARD', (
            'Get error, expected SAI_PACKET_ACTION_FORWARD but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_nat_zone_id_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': ['SAI_ROUTER_INTERFACE_ATTR_NAT_ZONE_ID', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_router_interface_attr_nat_zone_id_set'])
    def test_sai_router_interface_attr_nat_zone_id_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_NAT_ZONE_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_disable_decrement_ttl_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': [
                    'SAI_ROUTER_INTERFACE_ATTR_DISABLE_DECREMENT_TTL',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_disable_decrement_ttl_set']
    )
    def test_sai_router_interface_attr_disable_decrement_ttl_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_DISABLE_DECREMENT_TTL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_router_interface_attr_admin_mpls_state_set(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'atrribute': ['SAI_ROUTER_INTERFACE_ATTR_ADMIN_MPLS_STATE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_router_interface_attr_admin_mpls_state_set']
    )
    def test_sai_router_interface_attr_admin_mpls_state_get(self, npu):
        commands = [
            {
                'name': 'router_interface_1',
                'op': 'get',
                'attributes': ['SAI_ROUTER_INTERFACE_ATTR_ADMIN_MPLS_STATE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    def test_router_interface_remove(self, npu):
        commands = [
            {'name': 'router_interface_1', 'op': 'remove'},
            {'name': 'bridge_1', 'op': 'remove'},
            {'name': 'vlan_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
            {'name': 'virtual_router_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
