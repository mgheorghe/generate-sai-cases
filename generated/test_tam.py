from pprint import pprint

import pytest


class TestSaiTam:
    # object with no attributes

    def test_tam_create(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tam_attr_telemetry_objects_list_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_attr_telemetry_objects_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'atrribute': ['SAI_TAM_ATTR_TELEMETRY_OBJECTS_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_attr_telemetry_objects_list_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_attr_telemetry_objects_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'atrribute': 'SAI_TAM_ATTR_TELEMETRY_OBJECTS_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_tam_attr_event_objects_list_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_attr_event_objects_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'atrribute': ['SAI_TAM_ATTR_EVENT_OBJECTS_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_attr_event_objects_list_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_attr_event_objects_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'atrribute': 'SAI_TAM_ATTR_EVENT_OBJECTS_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_tam_attr_int_objects_list_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_attr_int_objects_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'atrribute': ['SAI_TAM_ATTR_INT_OBJECTS_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_attr_int_objects_list_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_attr_int_objects_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'atrribute': 'SAI_TAM_ATTR_INT_OBJECTS_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_tam_remove(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
