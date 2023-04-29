from pprint import pprint

import pytest


class TestSaiTamTelemetry:
    # object with parent SAI_OBJECT_TYPE_TAM_COLLECTOR

    @pytest.mark.dependency(scope='session')
    def test_tam_telemetry_create(self, npu):
        commands = [
            {
                'name': 'tam_telemetry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'attributes': [
                    'SAI_TAM_TELEMETRY_ATTR_COLLECTOR_LIST',
                    'sai_object_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tam_telemetry_attr_tam_type_list_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_telemetry_attr_tam_type_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'atrribute': ['SAI_TAM_TELEMETRY_ATTR_TAM_TYPE_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_telemetry_attr_tam_type_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_telemetry_attr_tam_type_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'atrribute': 'SAI_TAM_TELEMETRY_ATTR_TAM_TYPE_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_tam_telemetry_attr_tam_reporting_unit_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_telemetry_attr_tam_reporting_unit_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'atrribute': [
                    'SAI_TAM_TELEMETRY_ATTR_TAM_REPORTING_UNIT',
                    'SAI_TAM_REPORTING_UNIT_SEC',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_telemetry_attr_tam_reporting_unit_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_telemetry_attr_tam_reporting_unit_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'atrribute': 'SAI_TAM_TELEMETRY_ATTR_TAM_REPORTING_UNIT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_TAM_REPORTING_UNIT_SEC' for result in results]
        ), 'Get error'

    def test_sai_tam_telemetry_attr_reporting_interval_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_telemetry_attr_reporting_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'atrribute': ['SAI_TAM_TELEMETRY_ATTR_REPORTING_INTERVAL', '1'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_telemetry_attr_reporting_interval_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_telemetry_attr_reporting_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'atrribute': 'SAI_TAM_TELEMETRY_ATTR_REPORTING_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1' for result in results]), 'Get error'

    def test_tam_telemetry_remove(self, npu):
        commands = [
            {
                'name': 'tam_telemetry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_TELEMETRY',
                'attributes': [
                    'SAI_TAM_TELEMETRY_ATTR_COLLECTOR_LIST',
                    'sai_object_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
