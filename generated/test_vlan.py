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
            {'name': 'vlan_1', 'op': 'get', 'attributes': ['SAI_VLAN_ATTR_MEMBER_LIST']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_max_learned_addresses_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_MAX_LEARNED_ADDRESSES', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_max_learned_addresses_set'])
    def test_sai_vlan_attr_max_learned_addresses_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_MAX_LEARNED_ADDRESSES'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_stp_instance_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_STP_INSTANCE',
                    'attrvalue SAI_SWITCH_ATTR_DEFAULT_STP_INST_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_stp_instance_set'])
    def test_sai_vlan_attr_stp_instance_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_STP_INSTANCE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[0][0].value() == 'attrvalue SAI_SWITCH_ATTR_DEFAULT_STP_INST_ID'
        ), (
            'Get error, expected attrvalue SAI_SWITCH_ATTR_DEFAULT_STP_INST_ID but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_learn_disable_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_LEARN_DISABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_learn_disable_set'])
    def test_sai_vlan_attr_learn_disable_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_LEARN_DISABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_ipv4_mcast_lookup_key_type_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_IPV4_MCAST_LOOKUP_KEY_TYPE',
                    'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_ipv4_mcast_lookup_key_type_set']
    )
    def test_sai_vlan_attr_ipv4_mcast_lookup_key_type_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_IPV4_MCAST_LOOKUP_KEY_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA', (
            'Get error, expected SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_ipv6_mcast_lookup_key_type_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_IPV6_MCAST_LOOKUP_KEY_TYPE',
                    'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_ipv6_mcast_lookup_key_type_set']
    )
    def test_sai_vlan_attr_ipv6_mcast_lookup_key_type_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_IPV6_MCAST_LOOKUP_KEY_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA', (
            'Get error, expected SAI_VLAN_MCAST_LOOKUP_KEY_TYPE_MAC_DA but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_non_ip_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_NON_IP_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_non_ip_mcast_output_group_id_set']
    )
    def test_sai_vlan_attr_unknown_non_ip_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_NON_IP_MCAST_OUTPUT_GROUP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_ipv4_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_IPV4_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_ipv4_mcast_output_group_id_set']
    )
    def test_sai_vlan_attr_unknown_ipv4_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_IPV4_MCAST_OUTPUT_GROUP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_ipv6_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_IPV6_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_ipv6_mcast_output_group_id_set']
    )
    def test_sai_vlan_attr_unknown_ipv6_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_IPV6_MCAST_OUTPUT_GROUP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_linklocal_mcast_output_group_id_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_LINKLOCAL_MCAST_OUTPUT_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_linklocal_mcast_output_group_id_set']
    )
    def test_sai_vlan_attr_unknown_linklocal_mcast_output_group_id_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_LINKLOCAL_MCAST_OUTPUT_GROUP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_ingress_acl_set'])
    def test_sai_vlan_attr_ingress_acl_get(self, npu):
        commands = [
            {'name': 'vlan_1', 'op': 'get', 'attributes': ['SAI_VLAN_ATTR_INGRESS_ACL']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_egress_acl_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_EGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_egress_acl_set'])
    def test_sai_vlan_attr_egress_acl_get(self, npu):
        commands = [
            {'name': 'vlan_1', 'op': 'get', 'attributes': ['SAI_VLAN_ATTR_EGRESS_ACL']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_META_DATA', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_meta_data_set'])
    def test_sai_vlan_attr_meta_data_get(self, npu):
        commands = [
            {'name': 'vlan_1', 'op': 'get', 'attributes': ['SAI_VLAN_ATTR_META_DATA']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_unicast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE',
                    'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_unicast_flood_control_type_set']
    )
    def test_sai_vlan_attr_unknown_unicast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL', (
            'Get error, expected SAI_VLAN_FLOOD_CONTROL_TYPE_ALL but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_unicast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_unicast_flood_group_set']
    )
    def test_sai_vlan_attr_unknown_unicast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_multicast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE',
                    'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_multicast_flood_control_type_set']
    )
    def test_sai_vlan_attr_unknown_multicast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL', (
            'Get error, expected SAI_VLAN_FLOOD_CONTROL_TYPE_ALL but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_unknown_multicast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_unknown_multicast_flood_group_set']
    )
    def test_sai_vlan_attr_unknown_multicast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_broadcast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_BROADCAST_FLOOD_CONTROL_TYPE',
                    'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_broadcast_flood_control_type_set']
    )
    def test_sai_vlan_attr_broadcast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_BROADCAST_FLOOD_CONTROL_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_VLAN_FLOOD_CONTROL_TYPE_ALL', (
            'Get error, expected SAI_VLAN_FLOOD_CONTROL_TYPE_ALL but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_broadcast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': [
                    'SAI_VLAN_ATTR_BROADCAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_broadcast_flood_group_set'])
    def test_sai_vlan_attr_broadcast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_BROADCAST_FLOOD_GROUP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_custom_igmp_snooping_enable_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_CUSTOM_IGMP_SNOOPING_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_vlan_attr_custom_igmp_snooping_enable_set']
    )
    def test_sai_vlan_attr_custom_igmp_snooping_enable_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_CUSTOM_IGMP_SNOOPING_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_vlan_attr_tam_object_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'atrribute': ['SAI_VLAN_ATTR_TAM_OBJECT', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_tam_object_set'])
    def test_sai_vlan_attr_tam_object_get(self, npu):
        commands = [
            {'name': 'vlan_1', 'op': 'get', 'attributes': ['SAI_VLAN_ATTR_TAM_OBJECT']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'empty', (
            'Get error, expected empty but got %s' % results[1][0].value()
        )

    def test_vlan_remove(self, npu):
        commands = [{'name': 'vlan_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
