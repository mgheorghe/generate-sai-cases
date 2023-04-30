from pprint import pprint

import pytest


class TestSaiSwitch:
    # object with no parents

    def test_switch_create(self, npu):
        commands = [
            {
                'name': 'switch_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'attributes': [
                    'SAI_SWITCH_ATTR_INIT_SWITCH',
                    'True',
                    'SAI_SWITCH_ATTR_HARDWARE_ACCESS_BUS',
                    'SAI_SWITCH_HARDWARE_ACCESS_BUS_MDIO',
                    'SAI_SWITCH_ATTR_PLATFROM_CONTEXT',
                    '10',
                    'SAI_SWITCH_ATTR_REGISTER_READ',
                    'sai_switch_register_read_fn',
                    'SAI_SWITCH_ATTR_REGISTER_WRITE',
                    'sai_switch_register_write_fn',
                    'SAI_SWITCH_ATTR_SWITCH_ID',
                    '10',
                    'SAI_SWITCH_ATTR_MAX_SYSTEM_CORES',
                    '10',
                    'SAI_SWITCH_ATTR_SYSTEM_PORT_CONFIG_LIST',
                    'sai_system_port_config_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_switch_attr_number_of_active_ports_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_active_ports_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_ACTIVE_PORTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_number_of_supported_ports_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_number_of_supported_ports_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_NUMBER_OF_SUPPORTED_PORTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_port_max_mtu_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_port_max_mtu_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PORT_MAX_MTU',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_cpu_port_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_cpu_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_CPU_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_max_virtual_routers_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_virtual_routers_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_VIRTUAL_ROUTERS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_table_size_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_table_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FDB_TABLE_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_l3_neighbor_table_size_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_l3_neighbor_table_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_L3_NEIGHBOR_TABLE_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_l3_route_table_size_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_l3_route_table_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_L3_ROUTE_TABLE_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_members_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_members_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_MEMBERS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_lags_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_lags_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_LAGS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_members_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_members_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_MEMBERS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_ecmp_groups_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_ecmp_groups_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_ECMP_GROUPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_unicast_queues_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_unicast_queues_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_UNICAST_QUEUES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_multicast_queues_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_multicast_queues_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_MULTICAST_QUEUES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_queues_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_queues_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_QUEUES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_cpu_queues_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_cpu_queues_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_CPU_QUEUES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_on_link_route_supported_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_on_link_route_supported_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ON_LINK_ROUTE_SUPPORTED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_oper_status_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_oper_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_OPER_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_number_of_temp_sensors_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_number_of_temp_sensors_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_NUMBER_OF_TEMP_SENSORS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_temp_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_temp_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_TEMP_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_temp_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_temp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_TEMP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_average_temp_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_average_temp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVERAGE_TEMP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_table_minimum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_table_minimum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_TABLE_MINIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_table_maximum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_table_maximum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_TABLE_MAXIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_entry_minimum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_entry_minimum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_ENTRY_MINIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_entry_maximum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_entry_maximum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_ENTRY_MAXIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_table_group_minimum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_table_group_minimum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_TABLE_GROUP_MINIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_table_group_maximum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_table_group_maximum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_TABLE_GROUP_MAXIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_dst_user_meta_data_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_dst_user_meta_data_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FDB_DST_USER_META_DATA_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_route_dst_user_meta_data_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_route_dst_user_meta_data_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ROUTE_DST_USER_META_DATA_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_neighbor_dst_user_meta_data_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_neighbor_dst_user_meta_data_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NEIGHBOR_DST_USER_META_DATA_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_port_user_meta_data_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_port_user_meta_data_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PORT_USER_META_DATA_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_vlan_user_meta_data_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_vlan_user_meta_data_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_VLAN_USER_META_DATA_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_user_meta_data_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_user_meta_data_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_USER_META_DATA_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_user_trap_id_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_user_trap_id_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_USER_TRAP_ID_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_default_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_default_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_DEFAULT_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_default_stp_inst_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_default_stp_inst_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_DEFAULT_STP_INST_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_max_stp_instance_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_stp_instance_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_STP_INSTANCE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_default_virtual_router_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_default_virtual_router_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_DEFAULT_VIRTUAL_ROUTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_default_override_virtual_router_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_default_override_virtual_router_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_DEFAULT_OVERRIDE_VIRTUAL_ROUTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_default_1q_bridge_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_default_1q_bridge_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_DEFAULT_1Q_BRIDGE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ingress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ingress_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ingress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_INGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_egress_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_egress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_EGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_egress_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_egress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_EGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_max_number_of_traffic_classes_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_max_number_of_traffic_classes_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_MAX_NUMBER_OF_TRAFFIC_CLASSES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_max_number_of_scheduler_group_hierarchy_levels_get(
        self, npu
    ):
        commands = [
            {
                'name': 'sai_switch_attr_qos_max_number_of_scheduler_group_hierarchy_levels_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_MAX_NUMBER_OF_SCHEDULER_GROUP_HIERARCHY_LEVELS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_max_number_of_scheduler_groups_per_hierarchy_level_get(
        self, npu
    ):
        commands = [
            {
                'name': 'sai_switch_attr_qos_max_number_of_scheduler_groups_per_hierarchy_level_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_MAX_NUMBER_OF_SCHEDULER_GROUPS_PER_HIERARCHY_LEVEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_max_number_of_childs_per_scheduler_group_get(
        self, npu
    ):
        commands = [
            {
                'name': 'sai_switch_attr_qos_max_number_of_childs_per_scheduler_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_MAX_NUMBER_OF_CHILDS_PER_SCHEDULER_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_total_buffer_size_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_total_buffer_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_TOTAL_BUFFER_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_ingress_buffer_pool_num_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ingress_buffer_pool_num_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_INGRESS_BUFFER_POOL_NUM',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_egress_buffer_pool_num_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_egress_buffer_pool_num_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_EGRESS_BUFFER_POOL_NUM',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_ipv4_route_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_ipv4_route_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_IPV4_ROUTE_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_ipv6_route_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_ipv6_route_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_IPV6_ROUTE_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_ipv4_nexthop_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_ipv4_nexthop_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_IPV4_NEXTHOP_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_ipv6_nexthop_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_ipv6_nexthop_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_IPV6_NEXTHOP_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_ipv4_neighbor_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_ipv4_neighbor_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_IPV4_NEIGHBOR_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_ipv6_neighbor_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_ipv6_neighbor_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_IPV6_NEIGHBOR_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_next_hop_group_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_next_hop_group_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_NEXT_HOP_GROUP_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_next_hop_group_member_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_next_hop_group_member_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_NEXT_HOP_GROUP_MEMBER_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_fdb_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_fdb_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_FDB_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_l2mc_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_l2mc_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_L2MC_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_ipmc_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_ipmc_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_IPMC_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_snat_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_snat_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_SNAT_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_dnat_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_dnat_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_DNAT_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_double_nat_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_double_nat_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_DOUBLE_NAT_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_acl_table_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_acl_table_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_ACL_TABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_acl_table_group_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_acl_table_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_ACL_TABLE_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_my_sid_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_my_sid_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_MY_SID_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_default_trap_group_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_default_trap_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_DEFAULT_TRAP_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_hash_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_hash_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_HASH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_hash_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_hash_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_HASH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_restart_warm_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_restart_warm_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_RESTART_WARM', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_restart_warm_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_restart_warm_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_RESTART_WARM',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_warm_recover_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_warm_recover_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_WARM_RECOVER', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_warm_recover_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_warm_recover_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_WARM_RECOVER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_restart_type_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_restart_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_RESTART_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_min_planned_restart_interval_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_min_planned_restart_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MIN_PLANNED_RESTART_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_nv_storage_size_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_nv_storage_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NV_STORAGE_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_acl_action_count_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_acl_action_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_ACL_ACTION_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_acl_range_count_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_acl_range_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_ACL_RANGE_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_capability_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_capability_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_CAPABILITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_mcast_snooping_capability_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_mcast_snooping_capability_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MCAST_SNOOPING_CAPABILITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_switching_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switching_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_SWITCHING_MODE',
                    'SAI_SWITCH_SWITCHING_MODE_STORE_AND_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_switching_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switching_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SWITCHING_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_SWITCH_SWITCHING_MODE_STORE_AND_FORWARD'
                for result in results
            ]
        ), 'Get error'

    def test_sai_switch_attr_bcast_cpu_flood_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_bcast_cpu_flood_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_BCAST_CPU_FLOOD_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_bcast_cpu_flood_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_bcast_cpu_flood_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_BCAST_CPU_FLOOD_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_mcast_cpu_flood_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_mcast_cpu_flood_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_MCAST_CPU_FLOOD_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_mcast_cpu_flood_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_mcast_cpu_flood_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MCAST_CPU_FLOOD_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_src_mac_address_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_src_mac_address_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_SRC_MAC_ADDRESS', 'vendor'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_src_mac_address_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_src_mac_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SRC_MAC_ADDRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'vendor' for result in results]), 'Get error'

    def test_sai_switch_attr_max_learned_addresses_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_learned_addresses_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_MAX_LEARNED_ADDRESSES', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_max_learned_addresses_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_learned_addresses_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_LEARNED_ADDRESSES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_aging_time_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_aging_time_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_FDB_AGING_TIME', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_aging_time_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_aging_time_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FDB_AGING_TIME',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_unicast_miss_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_unicast_miss_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_FDB_UNICAST_MISS_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_unicast_miss_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_unicast_miss_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FDB_UNICAST_MISS_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_switch_attr_fdb_broadcast_miss_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_broadcast_miss_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_FDB_BROADCAST_MISS_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_broadcast_miss_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_broadcast_miss_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FDB_BROADCAST_MISS_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_switch_attr_fdb_multicast_miss_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_multicast_miss_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_FDB_MULTICAST_MISS_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_multicast_miss_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_multicast_miss_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FDB_MULTICAST_MISS_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_switch_attr_ecmp_default_hash_algorithm_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_hash_algorithm_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_ECMP_DEFAULT_HASH_ALGORITHM',
                    'SAI_HASH_ALGORITHM_CRC',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_default_hash_algorithm_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_hash_algorithm_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_DEFAULT_HASH_ALGORITHM',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_HASH_ALGORITHM_CRC' for result in results]
        ), 'Get error'

    def test_sai_switch_attr_ecmp_default_hash_seed_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_hash_seed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ECMP_DEFAULT_HASH_SEED', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_default_hash_seed_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_hash_seed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_DEFAULT_HASH_SEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_default_hash_offset_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_hash_offset_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ECMP_DEFAULT_HASH_OFFSET', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_default_hash_offset_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_hash_offset_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_DEFAULT_HASH_OFFSET',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_default_symmetric_hash_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_symmetric_hash_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ECMP_DEFAULT_SYMMETRIC_HASH', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_default_symmetric_hash_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_default_symmetric_hash_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_DEFAULT_SYMMETRIC_HASH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_hash_ipv4_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_hash_ipv4_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ECMP_HASH_IPV4', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_hash_ipv4_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_hash_ipv4_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_HASH_IPV4',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_hash_ipv4_in_ipv4_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_hash_ipv4_in_ipv4_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_ECMP_HASH_IPV4_IN_IPV4',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_hash_ipv4_in_ipv4_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_hash_ipv4_in_ipv4_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_HASH_IPV4_IN_IPV4',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_hash_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_hash_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ECMP_HASH_IPV6', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_hash_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_hash_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_HASH_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_default_hash_algorithm_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_hash_algorithm_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_LAG_DEFAULT_HASH_ALGORITHM',
                    'SAI_HASH_ALGORITHM_CRC',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_default_hash_algorithm_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_hash_algorithm_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_DEFAULT_HASH_ALGORITHM',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_HASH_ALGORITHM_CRC' for result in results]
        ), 'Get error'

    def test_sai_switch_attr_lag_default_hash_seed_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_hash_seed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_LAG_DEFAULT_HASH_SEED', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_default_hash_seed_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_hash_seed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_DEFAULT_HASH_SEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_default_hash_offset_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_hash_offset_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_LAG_DEFAULT_HASH_OFFSET', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_default_hash_offset_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_hash_offset_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_DEFAULT_HASH_OFFSET',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_default_symmetric_hash_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_symmetric_hash_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_LAG_DEFAULT_SYMMETRIC_HASH', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_default_symmetric_hash_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_default_symmetric_hash_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_DEFAULT_SYMMETRIC_HASH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_hash_ipv4_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_hash_ipv4_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_LAG_HASH_IPV4', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_hash_ipv4_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_hash_ipv4_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_HASH_IPV4',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_hash_ipv4_in_ipv4_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_hash_ipv4_in_ipv4_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_LAG_HASH_IPV4_IN_IPV4',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_hash_ipv4_in_ipv4_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_hash_ipv4_in_ipv4_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_HASH_IPV4_IN_IPV4',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_hash_ipv6_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_hash_ipv6_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_LAG_HASH_IPV6', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_lag_hash_ipv6_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_lag_hash_ipv6_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_LAG_HASH_IPV6',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_counter_refresh_interval_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_counter_refresh_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_COUNTER_REFRESH_INTERVAL', '1'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_counter_refresh_interval_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_counter_refresh_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_COUNTER_REFRESH_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_default_tc_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_default_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_QOS_DEFAULT_TC', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_default_tc_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_default_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_DEFAULT_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dot1p_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dot1p_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_DOT1P_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dot1p_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dot1p_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_DOT1P_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dot1p_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dot1p_to_color_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_DOT1P_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dot1p_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dot1p_to_color_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_DOT1P_TO_COLOR_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dscp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dscp_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_DSCP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dscp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dscp_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_DSCP_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dscp_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dscp_to_color_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_DSCP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dscp_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dscp_to_color_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_DSCP_TO_COLOR_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_to_queue_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_TC_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_to_queue_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_TC_TO_QUEUE_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_and_color_to_dot1p_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_and_color_to_dot1p_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_TC_AND_COLOR_TO_DOT1P_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_and_color_to_dot1p_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_and_color_to_dot1p_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_TC_AND_COLOR_TO_DOT1P_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_and_color_to_dscp_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_and_color_to_dscp_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_TC_AND_COLOR_TO_DSCP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_and_color_to_dscp_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_and_color_to_dscp_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_TC_AND_COLOR_TO_DSCP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_shell_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_shell_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_SWITCH_SHELL_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_shell_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_shell_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SWITCH_SHELL_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_state_change_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_state_change_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_SWITCH_STATE_CHANGE_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_state_change_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_state_change_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SWITCH_STATE_CHANGE_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_shutdown_request_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_shutdown_request_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_SWITCH_SHUTDOWN_REQUEST_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_shutdown_request_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_shutdown_request_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SWITCH_SHUTDOWN_REQUEST_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_event_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_event_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_FDB_EVENT_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_fdb_event_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fdb_event_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FDB_EVENT_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_port_state_change_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_port_state_change_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_PORT_STATE_CHANGE_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_port_state_change_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_port_state_change_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PORT_STATE_CHANGE_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_packet_event_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_packet_event_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_PACKET_EVENT_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_packet_event_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_packet_event_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PACKET_EVENT_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_fast_api_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fast_api_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_FAST_API_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_fast_api_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fast_api_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FAST_API_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_mirror_tc_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_mirror_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_MIRROR_TC', '255'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_mirror_tc_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_mirror_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MIRROR_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '255' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_stage_ingress_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_stage_ingress_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_STAGE_INGRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_stage_egress_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_stage_egress_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_STAGE_EGRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_srv6_max_sid_depth_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_srv6_max_sid_depth_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SRV6_MAX_SID_DEPTH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_srv6_tlv_type_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_srv6_tlv_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SRV6_TLV_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_num_lossless_queues_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_num_lossless_queues_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_NUM_LOSSLESS_QUEUES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_queue_pfc_deadlock_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_queue_pfc_deadlock_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_QUEUE_PFC_DEADLOCK_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_queue_pfc_deadlock_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_queue_pfc_deadlock_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QUEUE_PFC_DEADLOCK_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_pfc_dlr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_dlr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_PFC_DLR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_pfc_dlr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_dlr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PFC_DLR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_DROP' for result in results]
        ), 'Get error'

    def test_sai_switch_attr_pfc_tc_dld_interval_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_tc_dld_interval_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PFC_TC_DLD_INTERVAL_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_pfc_tc_dld_interval_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_tc_dld_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_PFC_TC_DLD_INTERVAL', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_pfc_tc_dld_interval_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_tc_dld_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PFC_TC_DLD_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_switch_attr_pfc_tc_dlr_interval_range_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_tc_dlr_interval_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PFC_TC_DLR_INTERVAL_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_pfc_tc_dlr_interval_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_tc_dlr_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_PFC_TC_DLR_INTERVAL', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_pfc_tc_dlr_interval_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pfc_tc_dlr_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PFC_TC_DLR_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_switch_attr_supported_protected_object_type_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_supported_protected_object_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SUPPORTED_PROTECTED_OBJECT_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_tpid_outer_vlan_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tpid_outer_vlan_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_TPID_OUTER_VLAN', '0x88A8'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_tpid_outer_vlan_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tpid_outer_vlan_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_TPID_OUTER_VLAN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x88A8' for result in results]), 'Get error'

    def test_sai_switch_attr_tpid_inner_vlan_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tpid_inner_vlan_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_TPID_INNER_VLAN', '0x8100'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_tpid_inner_vlan_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tpid_inner_vlan_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_TPID_INNER_VLAN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x8100' for result in results]), 'Get error'

    def test_sai_switch_attr_crc_check_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_crc_check_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_CRC_CHECK_ENABLE', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_crc_check_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_crc_check_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_CRC_CHECK_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_switch_attr_crc_recalculation_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_crc_recalculation_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_CRC_RECALCULATION_ENABLE', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_crc_recalculation_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_crc_recalculation_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_CRC_RECALCULATION_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_switch_attr_bfd_session_state_change_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_bfd_session_state_change_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_BFD_SESSION_STATE_CHANGE_NOTIFY',
                    'NULL',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_bfd_session_state_change_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_bfd_session_state_change_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_BFD_SESSION_STATE_CHANGE_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_bfd_session_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_bfd_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_BFD_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_bfd_session_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_bfd_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_BFD_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_supported_ipv4_bfd_session_offload_type_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_supported_ipv4_bfd_session_offload_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SUPPORTED_IPV4_BFD_SESSION_OFFLOAD_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_supported_ipv6_bfd_session_offload_type_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_supported_ipv6_bfd_session_offload_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SUPPORTED_IPV6_BFD_SESSION_OFFLOAD_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_min_bfd_rx_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_min_bfd_rx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MIN_BFD_RX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_min_bfd_tx_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_min_bfd_tx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MIN_BFD_TX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_ecn_ect_threshold_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecn_ect_threshold_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ECN_ECT_THRESHOLD_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecn_ect_threshold_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecn_ect_threshold_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECN_ECT_THRESHOLD_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_vxlan_default_router_mac_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_vxlan_default_router_mac_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_VXLAN_DEFAULT_ROUTER_MAC', 'vendor'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_vxlan_default_router_mac_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_vxlan_default_router_mac_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_VXLAN_DEFAULT_ROUTER_MAC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'vendor' for result in results]), 'Get error'

    def test_sai_switch_attr_vxlan_default_port_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_vxlan_default_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_VXLAN_DEFAULT_PORT', '4789'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_vxlan_default_port_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_vxlan_default_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_VXLAN_DEFAULT_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '4789' for result in results]), 'Get error'

    def test_sai_switch_attr_max_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_mirror_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_MIRROR_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_sampled_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_sampled_mirror_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_SAMPLED_MIRROR_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_supported_extended_stats_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_supported_extended_stats_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SUPPORTED_EXTENDED_STATS_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_uninit_data_plane_on_removal_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_uninit_data_plane_on_removal_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_UNINIT_DATA_PLANE_ON_REMOVAL', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_uninit_data_plane_on_removal_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_uninit_data_plane_on_removal_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_UNINIT_DATA_PLANE_ON_REMOVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_switch_attr_tam_object_id_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tam_object_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_TAM_OBJECT_ID', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_tam_object_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tam_object_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_TAM_OBJECT_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_switch_attr_tam_event_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tam_event_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_TAM_EVENT_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_tam_event_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tam_event_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_TAM_EVENT_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_supported_object_type_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_supported_object_type_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SUPPORTED_OBJECT_TYPE_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_pre_shutdown_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pre_shutdown_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_PRE_SHUTDOWN', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_pre_shutdown_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pre_shutdown_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PRE_SHUTDOWN',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_nat_zone_counter_object_id_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_nat_zone_counter_object_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_NAT_ZONE_COUNTER_OBJECT_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_nat_zone_counter_object_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_nat_zone_counter_object_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NAT_ZONE_COUNTER_OBJECT_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_nat_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_nat_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_NAT_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_nat_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_nat_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NAT_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_register_read_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_register_read_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_REGISTER_READ', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_register_read_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_register_read_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_REGISTER_READ',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_register_write_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_register_write_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_REGISTER_WRITE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_register_write_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_register_write_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_REGISTER_WRITE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_download_execute_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_download_execute_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_FIRMWARE_DOWNLOAD_EXECUTE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_download_execute_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_download_execute_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FIRMWARE_DOWNLOAD_EXECUTE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_broadcast_stop_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_broadcast_stop_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_FIRMWARE_BROADCAST_STOP', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_broadcast_stop_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_broadcast_stop_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FIRMWARE_BROADCAST_STOP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_verify_and_init_switch_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_verify_and_init_switch_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_FIRMWARE_VERIFY_AND_INIT_SWITCH',
                    'false',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_verify_and_init_switch_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_verify_and_init_switch_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FIRMWARE_VERIFY_AND_INIT_SWITCH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_status_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FIRMWARE_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_major_version_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_major_version_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FIRMWARE_MAJOR_VERSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_firmware_minor_version_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_firmware_minor_version_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FIRMWARE_MINOR_VERSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_port_connector_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_port_connector_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PORT_CONNECTOR_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_propogate_port_state_from_line_to_system_port_support_get(
        self, npu
    ):
        commands = [
            {
                'name': 'sai_switch_attr_propogate_port_state_from_line_to_system_port_support_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PROPOGATE_PORT_STATE_FROM_LINE_TO_SYSTEM_PORT_SUPPORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_macsec_object_list_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_macsec_object_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_MACSEC_OBJECT_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_macsec_object_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_macsec_object_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MACSEC_OBJECT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_mpls_exp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_mpls_exp_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_MPLS_EXP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_mpls_exp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_mpls_exp_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_MPLS_EXP_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_mpls_exp_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_mpls_exp_to_color_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_MPLS_EXP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_mpls_exp_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_mpls_exp_to_color_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_MPLS_EXP_TO_COLOR_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_and_color_to_mpls_exp_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_and_color_to_mpls_exp_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_tc_and_color_to_mpls_exp_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_tc_and_color_to_mpls_exp_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_system_ports_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_system_ports_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_SYSTEM_PORTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_system_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_system_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SYSTEM_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_number_of_fabric_ports_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_number_of_fabric_ports_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NUMBER_OF_FABRIC_PORTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_fabric_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_fabric_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FABRIC_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_switch_attr_packet_dma_memory_pool_size_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_packet_dma_memory_pool_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PACKET_DMA_MEMORY_POOL_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_failover_config_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_failover_config_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_FAILOVER_CONFIG_MODE',
                    'SAI_SWITCH_FAILOVER_CONFIG_MODE_NO_HITLESS',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_failover_config_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_failover_config_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_FAILOVER_CONFIG_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_SWITCH_FAILOVER_CONFIG_MODE_NO_HITLESS'
                for result in results
            ]
        ), 'Get error'

    def test_sai_switch_attr_supported_failover_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_supported_failover_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SUPPORTED_FAILOVER_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_tunnel_objects_list_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tunnel_objects_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_TUNNEL_OBJECTS_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_tunnel_objects_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_tunnel_objects_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_TUNNEL_OBJECTS_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_switch_attr_packet_available_dma_memory_pool_size_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_packet_available_dma_memory_pool_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PACKET_AVAILABLE_DMA_MEMORY_POOL_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_pre_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pre_ingress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_PRE_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_pre_ingress_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_pre_ingress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_PRE_INGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_available_snapt_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_snapt_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_SNAPT_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_dnapt_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_dnapt_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_DNAPT_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_double_napt_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_double_napt_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_DOUBLE_NAPT_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_my_mac_table_minimum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_my_mac_table_minimum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MY_MAC_TABLE_MINIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_my_mac_table_maximum_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_my_mac_table_maximum_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MY_MAC_TABLE_MAXIMUM_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_my_mac_list_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_my_mac_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MY_MAC_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_installed_my_mac_entries_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_installed_my_mac_entries_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_INSTALLED_MY_MAC_ENTRIES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_available_my_mac_entries_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_available_my_mac_entries_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_AVAILABLE_MY_MAC_ENTRIES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_max_number_of_forwarding_classes_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_number_of_forwarding_classes_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_NUMBER_OF_FORWARDING_CLASSES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dscp_to_forwarding_class_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dscp_to_forwarding_class_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_DSCP_TO_FORWARDING_CLASS_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_dscp_to_forwarding_class_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_dscp_to_forwarding_class_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_DSCP_TO_FORWARDING_CLASS_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_mpls_exp_to_forwarding_class_map_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_mpls_exp_to_forwarding_class_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_QOS_MPLS_EXP_TO_FORWARDING_CLASS_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_qos_mpls_exp_to_forwarding_class_map_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_qos_mpls_exp_to_forwarding_class_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_QOS_MPLS_EXP_TO_FORWARDING_CLASS_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_ipsec_object_id_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ipsec_object_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_IPSEC_OBJECT_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ipsec_object_id_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ipsec_object_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_IPSEC_OBJECT_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_ipsec_sa_tag_tpid_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ipsec_sa_tag_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_IPSEC_SA_TAG_TPID', '0xFFFE'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ipsec_sa_tag_tpid_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ipsec_sa_tag_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_IPSEC_SA_TAG_TPID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0xFFFE' for result in results]), 'Get error'

    def test_sai_switch_attr_ipsec_sa_status_change_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ipsec_sa_status_change_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_IPSEC_SA_STATUS_CHANGE_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ipsec_sa_status_change_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ipsec_sa_status_change_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_IPSEC_SA_STATUS_CHANGE_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_nat_event_notify_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_nat_event_notify_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_NAT_EVENT_NOTIFY', 'NULL'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_nat_event_notify_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_nat_event_notify_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_NAT_EVENT_NOTIFY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'NULL' for result in results]), 'Get error'

    def test_sai_switch_attr_max_ecmp_member_count_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_max_ecmp_member_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_MAX_ECMP_MEMBER_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_member_count_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_member_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ECMP_MEMBER_COUNT', '64'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ecmp_member_count_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ecmp_member_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ECMP_MEMBER_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '64' for result in results]), 'Get error'

    def test_sai_switch_attr_ars_profile_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ars_profile_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_ARS_PROFILE', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_ars_profile_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_ars_profile_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ARS_PROFILE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_switch_attr_acl_stage_post_ingress_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_acl_stage_post_ingress_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_ACL_STAGE_POST_INGRESS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_switch_attr_credit_wd_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_credit_wd_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_CREDIT_WD', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_credit_wd_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_credit_wd_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_CREDIT_WD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_switch_attr_credit_wd_timer_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_credit_wd_timer_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_CREDIT_WD_TIMER', '500'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_credit_wd_timer_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_credit_wd_timer_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_CREDIT_WD_TIMER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '500' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_isolate_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_isolate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': ['SAI_SWITCH_ATTR_SWITCH_ISOLATE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_switch_isolate_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_switch_isolate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_SWITCH_ISOLATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_switch_attr_hostif_oper_status_update_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_hostif_oper_status_update_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': [
                    'SAI_SWITCH_ATTR_HOSTIF_OPER_STATUS_UPDATE_MODE',
                    'SAI_SWITCH_HOSTIF_OPER_STATUS_UPDATE_MODE_APPLICATION',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_switch_attr_hostif_oper_status_update_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_switch_attr_hostif_oper_status_update_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'atrribute': 'SAI_SWITCH_ATTR_HOSTIF_OPER_STATUS_UPDATE_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_SWITCH_HOSTIF_OPER_STATUS_UPDATE_MODE_APPLICATION'
                for result in results
            ]
        ), 'Get error'

    def test_switch_remove(self, npu):
        commands = [
            {
                'name': 'switch_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'attributes': [
                    'SAI_SWITCH_ATTR_INIT_SWITCH',
                    'True',
                    'SAI_SWITCH_ATTR_HARDWARE_ACCESS_BUS',
                    'SAI_SWITCH_HARDWARE_ACCESS_BUS_MDIO',
                    'SAI_SWITCH_ATTR_PLATFROM_CONTEXT',
                    '10',
                    'SAI_SWITCH_ATTR_REGISTER_READ',
                    'sai_switch_register_read_fn',
                    'SAI_SWITCH_ATTR_REGISTER_WRITE',
                    'sai_switch_register_write_fn',
                    'SAI_SWITCH_ATTR_SWITCH_ID',
                    '10',
                    'SAI_SWITCH_ATTR_MAX_SYSTEM_CORES',
                    '10',
                    'SAI_SWITCH_ATTR_SYSTEM_PORT_CONFIG_LIST',
                    'sai_system_port_config_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
