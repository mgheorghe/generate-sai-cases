from pprint import pprint

import pytest


class TestSaiGenericProgrammable:
    # object with no parents

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

    @pytest.mark.dependency()
    def test_sai_generic_programmable_attr_entry_set(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': ['SAI_GENERIC_PROGRAMMABLE_ATTR_ENTRY', 'vendor'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_generic_programmable_attr_entry_set'])
    def test_sai_generic_programmable_attr_entry_get(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': 'SAI_GENERIC_PROGRAMMABLE_ATTR_ENTRY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'vendor', (
            'Get error, expected vendor but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_generic_programmable_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': [
                    'SAI_GENERIC_PROGRAMMABLE_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_generic_programmable_attr_counter_id_set']
    )
    def test_sai_generic_programmable_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'atrribute': 'SAI_GENERIC_PROGRAMMABLE_ATTR_COUNTER_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

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
