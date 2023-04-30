from pprint import pprint

import pytest


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
                    'sai_uint8_t',
                    'SAI_TAM_INT_ATTR_INLINE',
                    'True',
                    'SAI_TAM_INT_ATTR_INT_PRESENCE_L3_PROTOCOL',
                    'sai_uint8_t',
                    'SAI_TAM_INT_ATTR_REPORT_ID',
                    '$tam_report_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tam_int_attr_ioam_trace_type_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_ioam_trace_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_IOAM_TRACE_TYPE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_ioam_trace_type_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_ioam_trace_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_IOAM_TRACE_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_trace_vector_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_trace_vector_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_TRACE_VECTOR', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_trace_vector_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_trace_vector_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_TRACE_VECTOR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_action_vector_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_action_vector_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_ACTION_VECTOR', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_action_vector_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_action_vector_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_ACTION_VECTOR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_p4_int_instruction_bitmap_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_p4_int_instruction_bitmap_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_P4_INT_INSTRUCTION_BITMAP', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_p4_int_instruction_bitmap_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_p4_int_instruction_bitmap_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_P4_INT_INSTRUCTION_BITMAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_metadata_fragment_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_metadata_fragment_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_METADATA_FRAGMENT_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_metadata_fragment_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_metadata_fragment_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_METADATA_FRAGMENT_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_tam_int_attr_metadata_checksum_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_metadata_checksum_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_METADATA_CHECKSUM_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_metadata_checksum_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_metadata_checksum_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_METADATA_CHECKSUM_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_tam_int_attr_report_all_packets_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_report_all_packets_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_REPORT_ALL_PACKETS', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_report_all_packets_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_report_all_packets_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_REPORT_ALL_PACKETS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_tam_int_attr_flow_liveness_period_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_flow_liveness_period_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_FLOW_LIVENESS_PERIOD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_flow_liveness_period_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_flow_liveness_period_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_FLOW_LIVENESS_PERIOD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_latency_sensitivity_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_latency_sensitivity_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_LATENCY_SENSITIVITY', '20'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_latency_sensitivity_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_latency_sensitivity_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_LATENCY_SENSITIVITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '20' for result in results]), 'Get error'

    def test_sai_tam_int_attr_acl_group_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_acl_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_ACL_GROUP', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_acl_group_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_acl_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_ACL_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_tam_int_attr_max_hop_count_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_max_hop_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_MAX_HOP_COUNT', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_max_hop_count_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_max_hop_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_MAX_HOP_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_max_length_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_max_length_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_MAX_LENGTH', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_max_length_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_max_length_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_MAX_LENGTH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_name_space_id_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_name_space_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_NAME_SPACE_ID', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_name_space_id_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_name_space_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_NAME_SPACE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_int_attr_name_space_id_global_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_name_space_id_global_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_NAME_SPACE_ID_GLOBAL', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_name_space_id_global_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_name_space_id_global_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_NAME_SPACE_ID_GLOBAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_tam_int_attr_ingress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_ingress_samplepacket_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': [
                    'SAI_TAM_INT_ATTR_INGRESS_SAMPLEPACKET_ENABLE',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_ingress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_ingress_samplepacket_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_INGRESS_SAMPLEPACKET_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_tam_int_attr_collector_list_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_collector_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_COLLECTOR_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_collector_list_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_collector_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_COLLECTOR_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_tam_int_attr_math_func_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_math_func_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': ['SAI_TAM_INT_ATTR_MATH_FUNC', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_int_attr_math_func_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_int_attr_math_func_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_INT',
                'atrribute': 'SAI_TAM_INT_ATTR_MATH_FUNC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_tam_int_remove(self, npu):
        commands = [
            {
                'name': 'tam_int_1',
                'op': 'remove',
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
                    'sai_uint8_t',
                    'SAI_TAM_INT_ATTR_INLINE',
                    'True',
                    'SAI_TAM_INT_ATTR_INT_PRESENCE_L3_PROTOCOL',
                    'sai_uint8_t',
                    'SAI_TAM_INT_ATTR_REPORT_ID',
                    '$tam_report_1',
                ],
            },
            {
                'name': 'tam_report_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
