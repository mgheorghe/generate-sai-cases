from pprint import pprint

import pytest


class TestSaiTamTelType:
    # object with parent SAI_OBJECT_TYPE_TAM_REPORT

    def test_tam_tel_type_create(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            },
            {
                'name': 'tam_tel_type_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'attributes': [
                    'SAI_TAM_TEL_TYPE_ATTR_TAM_TELEMETRY_TYPE',
                    'SAI_TAM_TELEMETRY_TYPE_NE',
                    'SAI_TAM_TEL_TYPE_ATTR_REPORT_ID',
                    '$tam_report_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_int_switch_identifier_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': ['SAI_TAM_TEL_TYPE_ATTR_INT_SWITCH_IDENTIFIER', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_int_switch_identifier_set']
    )
    def test_sai_tam_tel_type_attr_int_switch_identifier_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_INT_SWITCH_IDENTIFIER',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_port_stats_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_PORT_STATS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_port_stats_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_port_stats_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_PORT_STATS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_port_stats_ingress_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_PORT_STATS_INGRESS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_port_stats_ingress_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_port_stats_ingress_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_PORT_STATS_INGRESS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_port_stats_egress_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_PORT_STATS_EGRESS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_port_stats_egress_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_port_stats_egress_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_PORT_STATS_EGRESS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_virtual_queue_stats_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_VIRTUAL_QUEUE_STATS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_virtual_queue_stats_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_virtual_queue_stats_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_VIRTUAL_QUEUE_STATS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_output_queue_stats_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_OUTPUT_QUEUE_STATS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_output_queue_stats_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_output_queue_stats_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_OUTPUT_QUEUE_STATS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_mmu_stats_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': ['SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_MMU_STATS', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_mmu_stats_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_mmu_stats_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_MMU_STATS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_fabric_stats_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_FABRIC_STATS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_fabric_stats_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_fabric_stats_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_FABRIC_STATS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_filter_stats_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_FILTER_STATS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_tel_type_attr_switch_enable_filter_stats_set']
    )
    def test_sai_tam_tel_type_attr_switch_enable_filter_stats_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_FILTER_STATS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_switch_enable_resource_utilization_stats_set(
        self, npu
    ):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': [
                    'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_RESOURCE_UTILIZATION_STATS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=[
            'test_sai_tam_tel_type_attr_switch_enable_resource_utilization_stats_set'
        ]
    )
    def test_sai_tam_tel_type_attr_switch_enable_resource_utilization_stats_get(
        self, npu
    ):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_SWITCH_ENABLE_RESOURCE_UTILIZATION_STATS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_fabric_q_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': ['SAI_TAM_TEL_TYPE_ATTR_FABRIC_Q', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_tel_type_attr_fabric_q_set'])
    def test_sai_tam_tel_type_attr_fabric_q_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_FABRIC_Q',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_ne_enable_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': ['SAI_TAM_TEL_TYPE_ATTR_NE_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_tel_type_attr_ne_enable_set'])
    def test_sai_tam_tel_type_attr_ne_enable_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_NE_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_dscp_value_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': ['SAI_TAM_TEL_TYPE_ATTR_DSCP_VALUE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_tel_type_attr_dscp_value_set'])
    def test_sai_tam_tel_type_attr_dscp_value_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_DSCP_VALUE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_tel_type_attr_math_func_set(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': ['SAI_TAM_TEL_TYPE_ATTR_MATH_FUNC', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_tel_type_attr_math_func_set'])
    def test_sai_tam_tel_type_attr_math_func_get(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'atrribute': 'SAI_TAM_TEL_TYPE_ATTR_MATH_FUNC',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_tam_tel_type_remove(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'attributes': [
                    'SAI_TAM_TEL_TYPE_ATTR_TAM_TELEMETRY_TYPE',
                    'SAI_TAM_TELEMETRY_TYPE_NE',
                    'SAI_TAM_TEL_TYPE_ATTR_REPORT_ID',
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
