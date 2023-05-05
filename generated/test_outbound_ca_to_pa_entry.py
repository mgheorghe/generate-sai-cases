from pprint import pprint

import pytest


class TestSaiOutboundCaToPaEntry:
    # object with no attributes

    def test_outbound_ca_to_pa_entry_create(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'attributes': [],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'dst_vnet_id': 'TODO',
                    'dip': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(
        name='test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_set'
    )
    def test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_set(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_set']
    )
    def test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_get(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set'
    )
    def test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC',
                    '0:0:0:0:0:0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set']
    )
    def test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_get(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0:0:0:0:0:0', (
            'Get error, expected 0:0:0:0:0:0 but got %s' % r_value
        )

    @pytest.mark.dependency(
        name='test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set'
    )
    def test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set']
    )
    def test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_get(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_outbound_ca_to_pa_entry_attr_counter_id_set')
    def test_sai_outbound_ca_to_pa_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_outbound_ca_to_pa_entry_attr_counter_id_set']
    )
    def test_sai_outbound_ca_to_pa_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'get',
                'attributes': ['SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_COUNTER_ID'],
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

    def test_outbound_ca_to_pa_entry_remove(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'dst_vnet_id': 'TODO',
                    'dip': 'TODO',
                },
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
