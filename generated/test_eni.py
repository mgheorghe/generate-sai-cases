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

    def test_sai_eni_attr_cps_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_cps_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_CPS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_cps_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_cps_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_CPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_eni_attr_pps_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_pps_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_PPS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_pps_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_pps_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_PPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_eni_attr_flows_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_flows_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_FLOWS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_flows_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_flows_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_FLOWS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_eni_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_admin_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_admin_state_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_admin_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_ADMIN_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_eni_attr_vm_underlay_dip_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_vm_underlay_dip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_VM_UNDERLAY_DIP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_vm_underlay_dip_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_vm_underlay_dip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_VM_UNDERLAY_DIP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_eni_attr_vm_vni_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_vm_vni_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_VM_VNI', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_vm_vni_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_vm_vni_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_VM_VNI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_eni_attr_vnet_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_vnet_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': ['SAI_ENI_ATTR_VNET_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_vnet_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_vnet_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_VNET_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'atrribute': 'SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

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
