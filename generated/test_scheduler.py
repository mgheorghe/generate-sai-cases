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

    def test_sai_scheduler_attr_scheduling_type_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_scheduling_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': [
                    'SAI_SCHEDULER_ATTR_SCHEDULING_TYPE',
                    'SAI_SCHEDULING_TYPE_WRR',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_attr_scheduling_type_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_scheduling_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_SCHEDULING_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_SCHEDULING_TYPE_WRR' for result in results]
        ), 'Get error'

    def test_sai_scheduler_attr_scheduling_weight_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_scheduling_weight_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_SCHEDULING_WEIGHT', '1'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_attr_scheduling_weight_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_scheduling_weight_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_SCHEDULING_WEIGHT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1' for result in results]), 'Get error'

    def test_sai_scheduler_attr_meter_type_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_meter_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_METER_TYPE', 'SAI_METER_TYPE_BYTES'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_attr_meter_type_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_meter_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_METER_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_METER_TYPE_BYTES' for result in results]
        ), 'Get error'

    def test_sai_scheduler_attr_min_bandwidth_rate_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_min_bandwidth_rate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_RATE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_attr_min_bandwidth_rate_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_min_bandwidth_rate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_RATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_scheduler_attr_min_bandwidth_burst_rate_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_min_bandwidth_burst_rate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_BURST_RATE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_attr_min_bandwidth_burst_rate_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_min_bandwidth_burst_rate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MIN_BANDWIDTH_BURST_RATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_scheduler_attr_max_bandwidth_rate_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_max_bandwidth_rate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_RATE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_attr_max_bandwidth_rate_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_max_bandwidth_rate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_RATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_scheduler_attr_max_bandwidth_burst_rate_set(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_max_bandwidth_burst_rate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': ['SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_BURST_RATE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_scheduler_attr_max_bandwidth_burst_rate_get(self, npu):
        commands = [
            {
                'name': 'sai_scheduler_attr_max_bandwidth_burst_rate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER',
                'atrribute': 'SAI_SCHEDULER_ATTR_MAX_BANDWIDTH_BURST_RATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

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
