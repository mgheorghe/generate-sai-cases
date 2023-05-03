from pprint import pprint

import pytest


class TestSaiScheduler:
    # object with no attributes

    def test_scheduler_create(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_scheduler_attr_scheduling_type_set(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': [
                    'SAI_SCHEDULER_ATTR_SCHEDULING_TYPE',
                    'SAI_SCHEDULING_TYPE_WRR',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_scheduler_attr_scheduling_type_set'])
    def test_sai_scheduler_attr_scheduling_type_get(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_SCHEDULING_TYPE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_SCHEDULING_TYPE_WRR', (
            'Get error, expected SAI_SCHEDULING_TYPE_WRR but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_scheduler_attr_scheduling_weight_set(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_SCHEDULING_WEIGHT', '1'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_scheduler_attr_scheduling_weight_set'])
    def test_sai_scheduler_attr_scheduling_weight_get(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_SCHEDULING_WEIGHT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '1', (
            'Get error, expected 1 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_scheduler_attr_meter_type_set(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_METER_TYPE', 'SAI_METER_TYPE_BYTES'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_scheduler_attr_meter_type_set'])
    def test_sai_scheduler_attr_meter_type_get(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_METER_TYPE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_METER_TYPE_BYTES', (
            'Get error, expected SAI_METER_TYPE_BYTES but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_scheduler_attr_min_bandwidth_rate_set(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_RATE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_scheduler_attr_min_bandwidth_rate_set'])
    def test_sai_scheduler_attr_min_bandwidth_rate_get(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_RATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_scheduler_attr_min_bandwidth_burst_rate_set(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_BURST_RATE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_scheduler_attr_min_bandwidth_burst_rate_set']
    )
    def test_sai_scheduler_attr_min_bandwidth_burst_rate_get(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_BURST_RATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_scheduler_attr_max_bandwidth_rate_set(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_RATE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_scheduler_attr_max_bandwidth_rate_set'])
    def test_sai_scheduler_attr_max_bandwidth_rate_get(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_RATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_scheduler_attr_max_bandwidth_burst_rate_set(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_BURST_RATE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_scheduler_attr_max_bandwidth_burst_rate_set']
    )
    def test_sai_scheduler_attr_max_bandwidth_burst_rate_get(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_BURST_RATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    def test_scheduler_remove(self, npu):
        commands = [
            {
                'name': 'scheduler_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
