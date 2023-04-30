from pprint import pprint

import pytest


class TestSaiLag:
    # object with no attributes

    def test_lag_create(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_lag_attr_port_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_lag_attr_ingress_acl_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_ingress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_ingress_acl_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_ingress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_INGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_lag_attr_egress_acl_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_egress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_EGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_egress_acl_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_egress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_EGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_lag_attr_port_vlan_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_port_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_PORT_VLAN_ID', '1'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_port_vlan_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_port_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_PORT_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1' for result in results]), 'Get error'

    def test_sai_lag_attr_default_vlan_priority_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_default_vlan_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_DEFAULT_VLAN_PRIORITY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_default_vlan_priority_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_default_vlan_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_DEFAULT_VLAN_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_lag_attr_drop_untagged_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_drop_untagged_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_DROP_UNTAGGED', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_drop_untagged_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_drop_untagged_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_DROP_UNTAGGED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_lag_attr_drop_tagged_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_drop_tagged_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_DROP_TAGGED', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_drop_tagged_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_drop_tagged_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_DROP_TAGGED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_lag_attr_tpid_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_TPID', '0x8100'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_tpid_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_TPID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x8100' for result in results]), 'Get error'

    def test_sai_lag_attr_label_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_LABEL', '""'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_label_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '""' for result in results]), 'Get error'

    def test_sai_lag_attr_ars_object_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_ars_object_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_ARS_OBJECT_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_attr_ars_object_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_ars_object_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_ARS_OBJECT_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_lag_attr_ars_packet_drops_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_ars_packet_drops_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_ARS_PACKET_DROPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_lag_attr_ars_port_reassignments_get(self, dpu):
        commands = [
            {
                'name': 'sai_lag_attr_ars_port_reassignments_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_ARS_PORT_REASSIGNMENTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_lag_remove(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
