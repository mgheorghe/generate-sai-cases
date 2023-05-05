from pprint import pprint

import pytest


class TestSaiNextHopGroupMember:
    # object with parent SAI_OBJECT_TYPE_NEXT_HOP_GROUP SAI_OBJECT_TYPE_NEXT_HOP SAI_OBJECT_TYPE_NEXT_HOP_GROUP

    def test_next_hop_group_member_create(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_ATTR_TYPE',
                    'SAI_NEXT_HOP_GROUP_TYPE_DYNAMIC_UNORDERED_ECMP',
                ],
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
                    '180.0.0.1',
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
                'name': 'next_hop_group_member_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MEMBER',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_GROUP_ID',
                    '$next_hop_group_1',
                    'SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_ID',
                    '$next_hop_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_next_hop_group_member_attr_next_hop_id_set')
    def test_sai_next_hop_group_member_attr_next_hop_id_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'set',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_ID', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_next_hop_group_member_attr_next_hop_id_set']
    )
    def test_sai_next_hop_group_member_attr_next_hop_id_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_NEXT_HOP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_next_hop_group_member_attr_weight_set')
    def test_sai_next_hop_group_member_attr_weight_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'set',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_WEIGHT', '1'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_next_hop_group_member_attr_weight_set'])
    def test_sai_next_hop_group_member_attr_weight_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_WEIGHT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '1', 'Get error, expected 1 but got %s' % r_value

    def test_sai_next_hop_group_member_attr_observed_role_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_OBSERVED_ROLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_next_hop_group_member_attr_monitored_object_set'
    )
    def test_sai_next_hop_group_member_attr_monitored_object_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'set',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_MEMBER_ATTR_MONITORED_OBJECT',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_next_hop_group_member_attr_monitored_object_set']
    )
    def test_sai_next_hop_group_member_attr_monitored_object_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_MONITORED_OBJECT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_next_hop_group_member_attr_sequence_id_set')
    def test_sai_next_hop_group_member_attr_sequence_id_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'set',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_SEQUENCE_ID', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_next_hop_group_member_attr_sequence_id_set']
    )
    def test_sai_next_hop_group_member_attr_sequence_id_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_SEQUENCE_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_next_hop_group_member_attr_counter_id_set')
    def test_sai_next_hop_group_member_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'set',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_MEMBER_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_next_hop_group_member_attr_counter_id_set']
    )
    def test_sai_next_hop_group_member_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_COUNTER_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(
        name='test_sai_next_hop_group_member_attr_ars_alternate_path_set'
    )
    def test_sai_next_hop_group_member_attr_ars_alternate_path_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'set',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_MEMBER_ATTR_ARS_ALTERNATE_PATH',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_next_hop_group_member_attr_ars_alternate_path_set']
    )
    def test_sai_next_hop_group_member_attr_ars_alternate_path_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_member_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MEMBER_ATTR_ARS_ALTERNATE_PATH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    def test_next_hop_group_member_remove(self, npu):
        commands = [
            {'name': 'next_hop_group_member_1', 'op': 'remove'},
            {'name': 'next_hop_1', 'op': 'remove'},
            {'name': 'srv6_sidlist_1', 'op': 'remove'},
            {'name': 'tunnel_1', 'op': 'remove'},
            {'name': 'router_interface_1', 'op': 'remove'},
            {'name': 'bridge_1', 'op': 'remove'},
            {'name': 'vlan_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
            {'name': 'virtual_router_1', 'op': 'remove'},
            {'name': 'next_hop_group_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
