from pprint import pprint

import pytest


class TestSaiTamEventThreshold:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_tam_event_threshold_create(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tam_event_threshold_attr_high_watermark_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_high_watermark_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_HIGH_WATERMARK', '90'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_high_watermark_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_high_watermark_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_HIGH_WATERMARK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '90' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_low_watermark_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_low_watermark_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_LOW_WATERMARK', '10'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_low_watermark_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_low_watermark_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_LOW_WATERMARK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '10' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_latency_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_latency_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_LATENCY', '10'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_latency_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_latency_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_LATENCY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '10' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_rate_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_rate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_RATE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_rate_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_rate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_RATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_abs_value_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_abs_value_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_ABS_VALUE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_abs_value_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_abs_value_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_ABS_VALUE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_unit_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_unit_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': [
                    'SAI_TAM_EVENT_THRESHOLD_ATTR_UNIT',
                    'SAI_TAM_EVENT_THRESHOLD_UNIT_MSEC',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_threshold_attr_unit_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_threshold_attr_unit_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_UNIT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_TAM_EVENT_THRESHOLD_UNIT_MSEC' for result in results]
        ), 'Get error'

    def test_tam_event_threshold_remove(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
