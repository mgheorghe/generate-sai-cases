from pprint import pprint

import pytest


class TestSaiNatEntry:
    # object with no attributes

    def test_nat_entry_create(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'attributes': [],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'nat_type': 'TODO',
                    'data': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_nat_type_set')
    def test_sai_nat_entry_attr_nat_type_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_NAT_TYPE', 'SAI_NAT_TYPE_NONE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_nat_type_set'])
    def test_sai_nat_entry_attr_nat_type_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_NAT_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NAT_TYPE_NONE', (
            'Get error, expected SAI_NAT_TYPE_NONE but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_src_ip_set')
    def test_sai_nat_entry_attr_src_ip_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_SRC_IP', '0.0.0.0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_src_ip_set'])
    def test_sai_nat_entry_attr_src_ip_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_SRC_IP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_src_ip_mask_set')
    def test_sai_nat_entry_attr_src_ip_mask_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_SRC_IP_MASK', '0.0.0.0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_src_ip_mask_set'])
    def test_sai_nat_entry_attr_src_ip_mask_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_SRC_IP_MASK'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_vr_id_set')
    def test_sai_nat_entry_attr_vr_id_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_VR_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_vr_id_set'])
    def test_sai_nat_entry_attr_vr_id_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_VR_ID'],
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

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_dst_ip_set')
    def test_sai_nat_entry_attr_dst_ip_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_DST_IP', '0.0.0.0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_dst_ip_set'])
    def test_sai_nat_entry_attr_dst_ip_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_DST_IP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_dst_ip_mask_set')
    def test_sai_nat_entry_attr_dst_ip_mask_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_DST_IP_MASK', '0.0.0.0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_dst_ip_mask_set'])
    def test_sai_nat_entry_attr_dst_ip_mask_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_DST_IP_MASK'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_l4_src_port_set')
    def test_sai_nat_entry_attr_l4_src_port_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_L4_SRC_PORT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_l4_src_port_set'])
    def test_sai_nat_entry_attr_l4_src_port_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_L4_SRC_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_l4_dst_port_set')
    def test_sai_nat_entry_attr_l4_dst_port_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_L4_DST_PORT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_l4_dst_port_set'])
    def test_sai_nat_entry_attr_l4_dst_port_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_L4_DST_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_enable_packet_count_set')
    def test_sai_nat_entry_attr_enable_packet_count_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_ENABLE_PACKET_COUNT', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_enable_packet_count_set'])
    def test_sai_nat_entry_attr_enable_packet_count_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_ENABLE_PACKET_COUNT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_packet_count_set')
    def test_sai_nat_entry_attr_packet_count_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_PACKET_COUNT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_packet_count_set'])
    def test_sai_nat_entry_attr_packet_count_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_PACKET_COUNT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_enable_byte_count_set')
    def test_sai_nat_entry_attr_enable_byte_count_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_ENABLE_BYTE_COUNT', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_enable_byte_count_set'])
    def test_sai_nat_entry_attr_enable_byte_count_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_ENABLE_BYTE_COUNT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_byte_count_set')
    def test_sai_nat_entry_attr_byte_count_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_BYTE_COUNT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_byte_count_set'])
    def test_sai_nat_entry_attr_byte_count_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_BYTE_COUNT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_hit_bit_cor_set')
    def test_sai_nat_entry_attr_hit_bit_cor_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_HIT_BIT_COR', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_hit_bit_cor_set'])
    def test_sai_nat_entry_attr_hit_bit_cor_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_HIT_BIT_COR'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_hit_bit_set')
    def test_sai_nat_entry_attr_hit_bit_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_HIT_BIT', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_hit_bit_set'])
    def test_sai_nat_entry_attr_hit_bit_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_HIT_BIT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_nat_entry_attr_aging_time_set')
    def test_sai_nat_entry_attr_aging_time_set(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'set',
                'attributes': ['SAI_NAT_ENTRY_ATTR_AGING_TIME', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_nat_entry_attr_aging_time_set'])
    def test_sai_nat_entry_attr_aging_time_get(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'get',
                'attributes': ['SAI_NAT_ENTRY_ATTR_AGING_TIME'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_nat_entry_remove(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'nat_type': 'TODO',
                    'data': 'TODO',
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
