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

    def test_sai_lag_attr_port_list_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_PORT_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_ingress_acl_set'])
    def test_sai_lag_attr_ingress_acl_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_INGRESS_ACL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_egress_acl_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_EGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_egress_acl_set'])
    def test_sai_lag_attr_egress_acl_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_EGRESS_ACL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_port_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_PORT_VLAN_ID', '1'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_port_vlan_id_set'])
    def test_sai_lag_attr_port_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_PORT_VLAN_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '1', (
            'Get error, expected 1 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_default_vlan_priority_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_DEFAULT_VLAN_PRIORITY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_default_vlan_priority_set'])
    def test_sai_lag_attr_default_vlan_priority_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_DEFAULT_VLAN_PRIORITY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_drop_untagged_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_DROP_UNTAGGED', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_drop_untagged_set'])
    def test_sai_lag_attr_drop_untagged_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_DROP_UNTAGGED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_drop_tagged_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_DROP_TAGGED', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_drop_tagged_set'])
    def test_sai_lag_attr_drop_tagged_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_DROP_TAGGED',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_tpid_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_TPID', '0x8100'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_tpid_set'])
    def test_sai_lag_attr_tpid_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_TPID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0x8100', (
            'Get error, expected 0x8100 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_label_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_LABEL', '""'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_label_set'])
    def test_sai_lag_attr_label_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_LABEL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '""', (
            'Get error, expected "" but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_lag_attr_ars_object_id_set(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': ['SAI_LAG_ATTR_ARS_OBJECT_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_lag_attr_ars_object_id_set'])
    def test_sai_lag_attr_ars_object_id_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_ARS_OBJECT_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_sai_lag_attr_ars_packet_drops_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_ARS_PACKET_DROPS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_sai_lag_attr_ars_port_reassignments_get(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'atrribute': 'SAI_LAG_ATTR_ARS_PORT_REASSIGNMENTS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

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
