from pprint import pprint

import pytest


class TestSaiGenericProgrammable:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_generic_programmable_create(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'attributes': ['SAI_GENERIC_PROGRAMMABLE_ATTR_OBJECT_NAME', '2:10,11'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_generic_programmable_attr_entry_set(self, dpu):
        commands = [
            {
                'name': 'sai_generic_programmable_attr_entry_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': ['SAI_GENERIC_PROGRAMMABLE_ATTR_ENTRY', 'vendor'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_generic_programmable_attr_entry_get(self, dpu):
        commands = [
            {
                'name': 'sai_generic_programmable_attr_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': 'SAI_GENERIC_PROGRAMMABLE_ATTR_ENTRY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'vendor' for result in results]), 'Get error'

    def test_sai_generic_programmable_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_generic_programmable_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': [
                    'SAI_GENERIC_PROGRAMMABLE_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_generic_programmable_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_generic_programmable_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': 'SAI_GENERIC_PROGRAMMABLE_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_generic_programmable_remove(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'attributes': ['SAI_GENERIC_PROGRAMMABLE_ATTR_OBJECT_NAME', '2:10,11'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
