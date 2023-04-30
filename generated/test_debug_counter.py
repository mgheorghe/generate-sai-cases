from pprint import pprint

import pytest


class TestSaiDebugCounter:
    # object with no parents

    def test_debug_counter_create(self, npu):
        commands = [
            {
                'name': 'debug_counter_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'attributes': [
                    'SAI_DEBUG_COUNTER_ATTR_TYPE',
                    'SAI_DEBUG_COUNTER_TYPE_PORT_IN_DROP_REASONS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_debug_counter_attr_index_get(self, npu):
        commands = [
            {
                'name': 'sai_debug_counter_attr_index_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'atrribute': 'SAI_DEBUG_COUNTER_ATTR_INDEX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_debug_counter_attr_in_drop_reason_list_set(self, npu):
        commands = [
            {
                'name': 'sai_debug_counter_attr_in_drop_reason_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'atrribute': ['SAI_DEBUG_COUNTER_ATTR_IN_DROP_REASON_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_debug_counter_attr_in_drop_reason_list_get(self, npu):
        commands = [
            {
                'name': 'sai_debug_counter_attr_in_drop_reason_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'atrribute': 'SAI_DEBUG_COUNTER_ATTR_IN_DROP_REASON_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_debug_counter_attr_out_drop_reason_list_set(self, npu):
        commands = [
            {
                'name': 'sai_debug_counter_attr_out_drop_reason_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'atrribute': ['SAI_DEBUG_COUNTER_ATTR_OUT_DROP_REASON_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_debug_counter_attr_out_drop_reason_list_get(self, npu):
        commands = [
            {
                'name': 'sai_debug_counter_attr_out_drop_reason_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'atrribute': 'SAI_DEBUG_COUNTER_ATTR_OUT_DROP_REASON_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_debug_counter_remove(self, npu):
        commands = [
            {
                'name': 'debug_counter_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'attributes': [
                    'SAI_DEBUG_COUNTER_ATTR_TYPE',
                    'SAI_DEBUG_COUNTER_TYPE_PORT_IN_DROP_REASONS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
