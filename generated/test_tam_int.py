from pprint import pprint

import pytest


class TestSaiTamInt:
    # object with parent SAI_OBJECT_TYPE_TAM_REPORT

    @pytest.mark.dependency(scope='session')
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
