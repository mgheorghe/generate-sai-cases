from pprint import pprint

import pytest


class TestSaiCounter:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_counter_create(self, npu):
        commands = [
            {
                'name': 'counter_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_COUNTER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_counter_attr_label_set(self, dpu):
        commands = [
            {
                'name': 'sai_counter_attr_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_COUNTER',
                'atrribute': ['SAI_COUNTER_ATTR_LABEL', '""'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_counter_attr_label_get(self, dpu):
        commands = [
            {
                'name': 'sai_counter_attr_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_COUNTER',
                'atrribute': 'SAI_COUNTER_ATTR_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '""' for result in results]), 'Get error'

    def test_counter_remove(self, npu):
        commands = [
            {
                'name': 'counter_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_COUNTER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
