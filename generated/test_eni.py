from pprint import pprint

import pytest


class TestSaiEni:
    # object with no attributes

    def test_eni_create(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_eni_attr_cps_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_CPS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_eni_attr_cps_set'])
    def test_sai_eni_attr_cps_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_CPS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_pps_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_PPS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_eni_attr_pps_set'])
    def test_sai_eni_attr_pps_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_PPS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_flows_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_FLOWS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_eni_attr_flows_set'])
    def test_sai_eni_attr_flows_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_FLOWS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_eni_attr_admin_state_set'])
    def test_sai_eni_attr_admin_state_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_ADMIN_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_vm_underlay_dip_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_VM_UNDERLAY_DIP', '0.0.0.0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_eni_attr_vm_underlay_dip_set'])
    def test_sai_eni_attr_vm_underlay_dip_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_VM_UNDERLAY_DIP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0.0.0.0', (
            'Get error, expected 0.0.0.0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_vm_vni_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_VM_VNI', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_eni_attr_vm_vni_set'])
    def test_sai_eni_attr_vm_vni_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_VM_VNI',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_vnet_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_VNET_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_eni_attr_vnet_id_set'])
    def test_sai_eni_attr_vnet_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_VNET_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_eni_remove(self, npu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
