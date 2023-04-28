from pprint import pprint

import pytest


class TestSaiTamTelType:
    # object with parent SAI_OBJECT_TYPE_TAM_REPORT

    @pytest.mark.dependency(scope='session')
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
                    'sai_tam_telemetry_type_t',
                    'SAI_TAM_TEL_TYPE_ATTR_REPORT_ID',
                    '$tam_report_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_tam_tel_type_remove(self, npu):
        commands = [
            {
                'name': 'tam_tel_type_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE',
                'attributes': [
                    'SAI_TAM_TEL_TYPE_ATTR_TAM_TELEMETRY_TYPE',
                    'sai_tam_telemetry_type_t',
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
