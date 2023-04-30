from pprint import pprint

import pytest


class TestSaiBridgePort:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_TUNNEL SAI_OBJECT_TYPE_BRIDGE

    def test_bridge_port_create(self, npu):
        commands = [
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
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_bridge_port_attr_tagging_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_tagging_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': [
                    'SAI_BRIDGE_PORT_ATTR_TAGGING_MODE',
                    'SAI_BRIDGE_PORT_TAGGING_MODE_TAGGED',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_tagging_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_tagging_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_TAGGING_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_BRIDGE_PORT_TAGGING_MODE_TAGGED' for result in results]
        ), 'Get error'

    def test_sai_bridge_port_attr_bridge_id_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_bridge_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': ['SAI_BRIDGE_PORT_ATTR_BRIDGE_ID', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_bridge_id_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_bridge_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_BRIDGE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_fdb_learning_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_fdb_learning_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': [
                    'SAI_BRIDGE_PORT_ATTR_FDB_LEARNING_MODE',
                    'SAI_BRIDGE_PORT_FDB_LEARNING_MODE_HW',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_fdb_learning_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_fdb_learning_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_FDB_LEARNING_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_BRIDGE_PORT_FDB_LEARNING_MODE_HW' for result in results]
        ), 'Get error'

    def test_sai_bridge_port_attr_max_learned_addresses_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_max_learned_addresses_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': ['SAI_BRIDGE_PORT_ATTR_MAX_LEARNED_ADDRESSES', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_max_learned_addresses_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_max_learned_addresses_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_MAX_LEARNED_ADDRESSES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_fdb_learning_limit_violation_packet_action_set(
        self, npu
    ):
        commands = [
            {
                'name': 'sai_bridge_port_attr_fdb_learning_limit_violation_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': [
                    'SAI_BRIDGE_PORT_ATTR_FDB_LEARNING_LIMIT_VIOLATION_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_fdb_learning_limit_violation_packet_action_get(
        self, npu
    ):
        commands = [
            {
                'name': 'sai_bridge_port_attr_fdb_learning_limit_violation_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_FDB_LEARNING_LIMIT_VIOLATION_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_DROP' for result in results]
        ), 'Get error'

    def test_sai_bridge_port_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_admin_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': ['SAI_BRIDGE_PORT_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_admin_state_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_admin_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_ADMIN_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_ingress_filtering_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_ingress_filtering_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': ['SAI_BRIDGE_PORT_ATTR_INGRESS_FILTERING', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_ingress_filtering_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_ingress_filtering_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_INGRESS_FILTERING',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_egress_filtering_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_egress_filtering_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': ['SAI_BRIDGE_PORT_ATTR_EGRESS_FILTERING', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_egress_filtering_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_egress_filtering_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_EGRESS_FILTERING',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_isolation_group_set(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_isolation_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': [
                    'SAI_BRIDGE_PORT_ATTR_ISOLATION_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_port_attr_isolation_group_get(self, npu):
        commands = [
            {
                'name': 'sai_bridge_port_attr_isolation_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'atrribute': 'SAI_BRIDGE_PORT_ATTR_ISOLATION_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_bridge_port_remove(self, npu):
        commands = [
            {
                'name': 'bridge_port_1',
                'op': 'remove',
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
                'name': 'virtual_router_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
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
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
