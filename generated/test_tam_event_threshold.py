from pprint import pprint

import pytest


class TestSaiTamEventThreshold:
    # object with no attributes

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

    @pytest.mark.dependency()
    def test_sai_tam_event_threshold_attr_high_watermark_set(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_HIGH_WATERMARK', '90'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_event_threshold_attr_high_watermark_set']
    )
    def test_sai_tam_event_threshold_attr_high_watermark_get(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_HIGH_WATERMARK',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '90', (
            'Get error, expected 90 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_event_threshold_attr_low_watermark_set(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_LOW_WATERMARK', '10'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_event_threshold_attr_low_watermark_set']
    )
    def test_sai_tam_event_threshold_attr_low_watermark_get(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_LOW_WATERMARK',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '10', (
            'Get error, expected 10 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_event_threshold_attr_latency_set(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_LATENCY', '10'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_event_threshold_attr_latency_set'])
    def test_sai_tam_event_threshold_attr_latency_get(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_LATENCY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '10', (
            'Get error, expected 10 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_event_threshold_attr_rate_set(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_RATE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_event_threshold_attr_rate_set'])
    def test_sai_tam_event_threshold_attr_rate_get(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_RATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_event_threshold_attr_abs_value_set(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': ['SAI_TAM_EVENT_THRESHOLD_ATTR_ABS_VALUE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_event_threshold_attr_abs_value_set'])
    def test_sai_tam_event_threshold_attr_abs_value_get(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_ABS_VALUE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_event_threshold_attr_unit_set(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': [
                    'SAI_TAM_EVENT_THRESHOLD_ATTR_UNIT',
                    'SAI_TAM_EVENT_THRESHOLD_UNIT_MSEC',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_event_threshold_attr_unit_set'])
    def test_sai_tam_event_threshold_attr_unit_get(self, npu):
        commands = [
            {
                'name': 'tam_event_threshold_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD',
                'atrribute': 'SAI_TAM_EVENT_THRESHOLD_ATTR_UNIT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_TAM_EVENT_THRESHOLD_UNIT_MSEC', (
            'Get error, expected SAI_TAM_EVENT_THRESHOLD_UNIT_MSEC but got %s'
            % results[1][0].value()
        )

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
