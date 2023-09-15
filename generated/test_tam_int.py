from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiTamInt:
    # object with parent SAI_OBJECT_TYPE_TAM_REPORT

    def test_tam_int_create(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            },
            {
                'name': 'tam_int_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'attributes': [
                    'SAI_TAM_INT_ATTR_TYPE',
                    'SAI_TAM_INT_TYPE_IOAM',
                    'SAI_TAM_INT_ATTR_DEVICE_ID',
                    '10',
                    'SAI_TAM_INT_ATTR_INT_PRESENCE_TYPE',
                    'SAI_TAM_INT_PRESENCE_TYPE_PB',
                    'SAI_TAM_INT_ATTR_INT_PRESENCE_PB1',
                    '10',
                    'SAI_TAM_INT_ATTR_INT_PRESENCE_PB2',
                    '10',
                    'SAI_TAM_INT_ATTR_INT_PRESENCE_DSCP_VALUE',
                    '1',
                    'SAI_TAM_INT_ATTR_INLINE',
                    'True',
                    'SAI_TAM_INT_ATTR_INT_PRESENCE_L3_PROTOCOL',
                    '1',
                    'SAI_TAM_INT_ATTR_REPORT_ID',
                    '$tam_report_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_tam_int_attr_ioam_trace_type_set')
    def test_sai_tam_int_attr_ioam_trace_type_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_IOAM_TRACE_TYPE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_ioam_trace_type_set'])
    def test_sai_tam_int_attr_ioam_trace_type_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_IOAM_TRACE_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_trace_vector_set')
    def test_sai_tam_int_attr_trace_vector_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_TRACE_VECTOR', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_trace_vector_set'])
    def test_sai_tam_int_attr_trace_vector_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_TRACE_VECTOR'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_action_vector_set')
    def test_sai_tam_int_attr_action_vector_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_ACTION_VECTOR', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_action_vector_set'])
    def test_sai_tam_int_attr_action_vector_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_ACTION_VECTOR'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_p4_int_instruction_bitmap_set')
    def test_sai_tam_int_attr_p4_int_instruction_bitmap_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_P4_INT_INSTRUCTION_BITMAP', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_tam_int_attr_p4_int_instruction_bitmap_set']
    )
    def test_sai_tam_int_attr_p4_int_instruction_bitmap_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_P4_INT_INSTRUCTION_BITMAP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_metadata_fragment_enable_set')
    def test_sai_tam_int_attr_metadata_fragment_enable_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_METADATA_FRAGMENT_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_tam_int_attr_metadata_fragment_enable_set']
    )
    def test_sai_tam_int_attr_metadata_fragment_enable_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_METADATA_FRAGMENT_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_metadata_checksum_enable_set')
    def test_sai_tam_int_attr_metadata_checksum_enable_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_METADATA_CHECKSUM_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_tam_int_attr_metadata_checksum_enable_set']
    )
    def test_sai_tam_int_attr_metadata_checksum_enable_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_METADATA_CHECKSUM_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_report_all_packets_set')
    def test_sai_tam_int_attr_report_all_packets_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_REPORT_ALL_PACKETS', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_report_all_packets_set'])
    def test_sai_tam_int_attr_report_all_packets_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_REPORT_ALL_PACKETS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_flow_liveness_period_set')
    def test_sai_tam_int_attr_flow_liveness_period_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_FLOW_LIVENESS_PERIOD', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_flow_liveness_period_set'])
    def test_sai_tam_int_attr_flow_liveness_period_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_FLOW_LIVENESS_PERIOD'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_latency_sensitivity_set')
    def test_sai_tam_int_attr_latency_sensitivity_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_LATENCY_SENSITIVITY', '20'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_latency_sensitivity_set'])
    def test_sai_tam_int_attr_latency_sensitivity_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_LATENCY_SENSITIVITY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '20', 'Get error, expected 20 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_acl_group_set')
    def test_sai_tam_int_attr_acl_group_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_ACL_GROUP', 'null'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_acl_group_set'])
    def test_sai_tam_int_attr_acl_group_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_ACL_GROUP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_max_hop_count_set')
    def test_sai_tam_int_attr_max_hop_count_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_MAX_HOP_COUNT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_max_hop_count_set'])
    def test_sai_tam_int_attr_max_hop_count_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_MAX_HOP_COUNT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_max_length_set')
    def test_sai_tam_int_attr_max_length_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_MAX_LENGTH', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_max_length_set'])
    def test_sai_tam_int_attr_max_length_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_MAX_LENGTH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_name_space_id_set')
    def test_sai_tam_int_attr_name_space_id_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_NAME_SPACE_ID', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_name_space_id_set'])
    def test_sai_tam_int_attr_name_space_id_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_NAME_SPACE_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_name_space_id_global_set')
    def test_sai_tam_int_attr_name_space_id_global_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_NAME_SPACE_ID_GLOBAL', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_name_space_id_global_set'])
    def test_sai_tam_int_attr_name_space_id_global_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_NAME_SPACE_ID_GLOBAL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_tam_int_attr_ingress_samplepacket_enable_set'
    )
    def test_sai_tam_int_attr_ingress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_INGRESS_SAMPLEPACKET_ENABLE', 'null'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_tam_int_attr_ingress_samplepacket_enable_set']
    )
    def test_sai_tam_int_attr_ingress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_INGRESS_SAMPLEPACKET_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_collector_list_set')
    def test_sai_tam_int_attr_collector_list_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_COLLECTOR_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_collector_list_set'])
    def test_sai_tam_int_attr_collector_list_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_COLLECTOR_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_int_attr_math_func_set')
    def test_sai_tam_int_attr_math_func_set(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'set',
                'attributes': ['SAI_TAM_INT_ATTR_MATH_FUNC', 'null'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_tam_int_attr_math_func_set'])
    def test_sai_tam_int_attr_math_func_get(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'get',
                'attributes': ['SAI_TAM_INT_ATTR_MATH_FUNC'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    def test_tam_int_remove(self, npu):
        commands = [
            {'name': 'tam_int_1', 'op': 'remove'},
            {'name': 'tam_report_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
