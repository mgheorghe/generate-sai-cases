from pprint import pprint

import pytest


class TestSaiCounter:
    # object with no attributes

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

    @pytest.mark.dependency(name='test_sai_counter_attr_label_set')
    def test_sai_counter_attr_label_set(self, npu):
        commands = [
            {
                'name': 'counter_1',
                'op': 'set',
                'attributes': ['SAI_COUNTER_ATTR_LABEL', '""'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_counter_attr_label_set'])
    def test_sai_counter_attr_label_get(self, npu):
        commands = [
            {'name': 'counter_1', 'op': 'get', 'attributes': ['SAI_COUNTER_ATTR_LABEL']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '""', 'Get error, expected "" but got %s' % r_value

    def test_counter_remove(self, npu):
        commands = [{'name': 'counter_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
