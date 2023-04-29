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
