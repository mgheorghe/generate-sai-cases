from pprint import pprint

import pytest


class TestSaiOutboundCaToPaEntry:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_outbound_ca_to_pa_entry_create(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_underlay_dip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP',
                    '0.0.0.0',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_underlay_dip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': 'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC',
                    '0:0:0:0:0:0',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_overlay_dmac_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': 'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0:0:0:0:0:0' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI',
                    'false',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': 'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': [
                    'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': 'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_outbound_ca_to_pa_entry_attr_ip_addr_family_get(self, dpu):
        commands = [
            {
                'name': 'sai_outbound_ca_to_pa_entry_attr_ip_addr_family_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'atrribute': 'SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_outbound_ca_to_pa_entry_remove(self, npu):
        commands = [
            {
                'name': 'outbound_ca_to_pa_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
