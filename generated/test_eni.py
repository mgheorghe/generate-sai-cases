from pprint import pprint

import pytest


@pytest.mark.dpu
class TestSaiEni:
    # object with no attributes

    def test_eni_create(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ENI',
                'attributes': [],
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_eni_attr_cps_set')
    def test_sai_eni_attr_cps_set(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'set', 'attributes': ['SAI_ENI_ATTR_CPS', '0']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_cps_set'])
    def test_sai_eni_attr_cps_get(self, dpu):
        commands = [{'name': 'eni_1', 'op': 'get', 'attributes': ['SAI_ENI_ATTR_CPS']}]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_pps_set')
    def test_sai_eni_attr_pps_set(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'set', 'attributes': ['SAI_ENI_ATTR_PPS', '0']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_pps_set'])
    def test_sai_eni_attr_pps_get(self, dpu):
        commands = [{'name': 'eni_1', 'op': 'get', 'attributes': ['SAI_ENI_ATTR_PPS']}]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_flows_set')
    def test_sai_eni_attr_flows_set(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'set', 'attributes': ['SAI_ENI_ATTR_FLOWS', '0']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_flows_set'])
    def test_sai_eni_attr_flows_get(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'get', 'attributes': ['SAI_ENI_ATTR_FLOWS']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_admin_state_set')
    def test_sai_eni_attr_admin_state_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': ['SAI_ENI_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_admin_state_set'])
    def test_sai_eni_attr_admin_state_get(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'get', 'attributes': ['SAI_ENI_ATTR_ADMIN_STATE']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_vm_underlay_dip_set')
    def test_sai_eni_attr_vm_underlay_dip_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': ['SAI_ENI_ATTR_VM_UNDERLAY_DIP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_vm_underlay_dip_set'])
    def test_sai_eni_attr_vm_underlay_dip_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_VM_UNDERLAY_DIP'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_vm_vni_set')
    def test_sai_eni_attr_vm_vni_set(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'set', 'attributes': ['SAI_ENI_ATTR_VM_VNI', '0']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_vm_vni_set'])
    def test_sai_eni_attr_vm_vni_get(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'get', 'attributes': ['SAI_ENI_ATTR_VM_VNI']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_vnet_id_set')
    def test_sai_eni_attr_vnet_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': ['SAI_ENI_ATTR_VNET_ID', 'null'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_vnet_id_set'])
    def test_sai_eni_attr_vnet_id_get(self, dpu):
        commands = [
            {'name': 'eni_1', 'op': 'get', 'attributes': ['SAI_ENI_ATTR_VNET_ID']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_v4_meter_policy_id_set')
    def test_sai_eni_attr_v4_meter_policy_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': ['SAI_ENI_ATTR_V4_METER_POLICY_ID', 'null'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_v4_meter_policy_id_set'])
    def test_sai_eni_attr_v4_meter_policy_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_V4_METER_POLICY_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_eni_attr_v6_meter_policy_id_set')
    def test_sai_eni_attr_v6_meter_policy_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': ['SAI_ENI_ATTR_V6_METER_POLICY_ID', 'null'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_eni_attr_v6_meter_policy_id_set'])
    def test_sai_eni_attr_v6_meter_policy_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_V6_METER_POLICY_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage1_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage2_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage3_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage4_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v4_stage5_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage1_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage2_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage3_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage4_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_inbound_v6_stage5_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage1_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage2_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage3_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage4_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v4_stage5_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage1_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage2_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage3_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage4_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_set'
    )
    def test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'set',
                'attributes': [
                    'SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID',
                    'null',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_set']
    )
    def test_sai_eni_attr_outbound_v6_stage5_dash_acl_group_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    def test_eni_remove(self, dpu):
        commands = [{'name': 'eni_1', 'op': 'remove'}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
