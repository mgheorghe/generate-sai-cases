from pprint import pprint

import pytest


class TestSaiNatEntry:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_nat_entry_create(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_nat_entry_attr_nat_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_nat_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_NAT_TYPE', 'SAI_NAT_TYPE_NONE'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_nat_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_nat_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_NAT_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NAT_TYPE_NONE' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_src_ip_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_src_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_SRC_IP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_src_ip_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_src_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_SRC_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_src_ip_mask_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_src_ip_mask_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_SRC_IP_MASK', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_src_ip_mask_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_src_ip_mask_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_SRC_IP_MASK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_vr_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_vr_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_VR_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_vr_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_vr_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_VR_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_dst_ip_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_dst_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_DST_IP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_dst_ip_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_dst_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_DST_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_dst_ip_mask_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_dst_ip_mask_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_DST_IP_MASK', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_dst_ip_mask_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_dst_ip_mask_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_DST_IP_MASK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_l4_src_port_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_l4_src_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_L4_SRC_PORT', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_l4_src_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_l4_src_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_L4_SRC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_l4_dst_port_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_l4_dst_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_L4_DST_PORT', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_l4_dst_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_l4_dst_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_L4_DST_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_enable_packet_count_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_enable_packet_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_ENABLE_PACKET_COUNT', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_enable_packet_count_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_enable_packet_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_ENABLE_PACKET_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_packet_count_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_packet_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_PACKET_COUNT', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_packet_count_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_packet_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_PACKET_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_enable_byte_count_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_enable_byte_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_ENABLE_BYTE_COUNT', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_enable_byte_count_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_enable_byte_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_ENABLE_BYTE_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_byte_count_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_byte_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_BYTE_COUNT', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_byte_count_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_byte_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_BYTE_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_hit_bit_cor_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_hit_bit_cor_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_HIT_BIT_COR', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_hit_bit_cor_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_hit_bit_cor_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_HIT_BIT_COR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_hit_bit_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_hit_bit_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_HIT_BIT', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_hit_bit_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_hit_bit_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_HIT_BIT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_aging_time_set(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_aging_time_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': ['SAI_NAT_ENTRY_ATTR_AGING_TIME', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_entry_attr_aging_time_get(self, dpu):
        commands = [
            {
                'name': 'sai_nat_entry_attr_aging_time_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'atrribute': 'SAI_NAT_ENTRY_ATTR_AGING_TIME',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_nat_entry_remove(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
