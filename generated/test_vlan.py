from pprint import pprint

import pytest


class TestSaiVlan:
    # object with no parents

    def test_vlan_create(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_vlan_attr_member_list_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_member_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_MEMBER_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_vlan_attr_max_learned_addresses_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_max_learned_addresses_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_MAX_LEARNED_ADDRESSES', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_max_learned_addresses_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_max_learned_addresses_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_MAX_LEARNED_ADDRESSES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_vlan_attr_stp_instance_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_stp_instance_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_STP_INSTANCE',
                    'attrvalue SAI_SWITCH_ATTR_DEFAULT_STP_INST_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_stp_instance_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_stp_instance_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_STP_INSTANCE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'attrvalue SAI_SWITCH_ATTR_DEFAULT_STP_INST_ID'
                for result in results
            ]
        ), 'Get error'

    def test_sai_vlan_attr_learn_disable_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_learn_disable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_LEARN_DISABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_learn_disable_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_learn_disable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_LEARN_DISABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_vlan_attr_ipv4_mcast_lookup_key_type_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_ipv4_mcast_lookup_key_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_IPV4_MCAST_LOOKUP_KEY_TYPE',
                    'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_ipv4_mcast_lookup_key_type_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_ipv4_mcast_lookup_key_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_IPV4_MCAST_LOOKUP_KEY_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA' for result in results]
        ), 'Get error'

    def test_sai_vlan_attr_ipv6_mcast_lookup_key_type_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_ipv6_mcast_lookup_key_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_IPV6_MCAST_LOOKUP_KEY_TYPE',
                    'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_ipv6_mcast_lookup_key_type_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_ipv6_mcast_lookup_key_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_IPV6_MCAST_LOOKUP_KEY_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA' for result in results]
        ), 'Get error'

    def test_sai_vlan_attr_unknown_non_ip_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_non_ip_mcast_output_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_NON_IP_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_non_ip_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_non_ip_mcast_output_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_NON_IP_MCAST_OUTPUT_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_ipv4_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_ipv4_mcast_output_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_IPV4_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_ipv4_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_ipv4_mcast_output_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_IPV4_MCAST_OUTPUT_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_ipv6_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_ipv6_mcast_output_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_IPV6_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_ipv6_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_ipv6_mcast_output_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_IPV6_MCAST_OUTPUT_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_linklocal_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_linklocal_mcast_output_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_LINKLOCAL_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_linklocal_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_linklocal_mcast_output_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_LINKLOCAL_MCAST_OUTPUT_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_ingress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_ingress_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_ingress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_INGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_egress_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_egress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_EGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_egress_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_egress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_EGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_meta_data_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_META_DATA', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_meta_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_META_DATA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_unicast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_unicast_flood_control_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE',
                    'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_unicast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_unicast_flood_control_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL' for result in results]
        ), 'Get error'

    def test_sai_vlan_attr_unknown_unicast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_unicast_flood_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_unicast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_unicast_flood_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_multicast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_multicast_flood_control_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE',
                    'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_multicast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_multicast_flood_control_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL' for result in results]
        ), 'Get error'

    def test_sai_vlan_attr_unknown_multicast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_multicast_flood_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_unknown_multicast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_unknown_multicast_flood_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_broadcast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_broadcast_flood_control_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_BROADCAST_FLOOD_CONTROL_TYPE',
                    'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_broadcast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_broadcast_flood_control_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_BROADCAST_FLOOD_CONTROL_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL' for result in results]
        ), 'Get error'

    def test_sai_vlan_attr_broadcast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_broadcast_flood_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_BROADCAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_broadcast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_broadcast_flood_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_BROADCAST_FLOOD_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_vlan_attr_custom_igmp_snooping_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_custom_igmp_snooping_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_CUSTOM_IGMP_SNOOPING_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_custom_igmp_snooping_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_custom_igmp_snooping_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_CUSTOM_IGMP_SNOOPING_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_vlan_attr_tam_object_set(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_tam_object_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_TAM_OBJECT', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vlan_attr_tam_object_get(self, npu):
        commands = [
            {
                'name': 'sai_vlan_attr_tam_object_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': 'SAI_VLAN_ATTR_TAM_OBJECT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_vlan_remove(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
