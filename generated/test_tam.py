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

    @pytest.mark.dependency(name='test_sai_tam_attr_telemetry_objects_list_set')
    def test_sai_tam_attr_telemetry_objects_list_set(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'set',
                'attributes': ['SAI_TAM_ATTR_TELEMETRY_OBJECTS_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_attr_telemetry_objects_list_set'])
    def test_sai_tam_attr_telemetry_objects_list_get(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'get',
                'attributes': ['SAI_TAM_ATTR_TELEMETRY_OBJECTS_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_attr_event_objects_list_set')
    def test_sai_tam_attr_event_objects_list_set(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'set',
                'attributes': ['SAI_TAM_ATTR_EVENT_OBJECTS_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_attr_event_objects_list_set'])
    def test_sai_tam_attr_event_objects_list_get(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'get',
                'attributes': ['SAI_TAM_ATTR_EVENT_OBJECTS_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_attr_int_objects_list_set')
    def test_sai_tam_attr_int_objects_list_set(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'set',
                'attributes': ['SAI_TAM_ATTR_INT_OBJECTS_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_attr_int_objects_list_set'])
    def test_sai_tam_attr_int_objects_list_get(self, npu):
        commands = [
            {
                'name': 'tam_1',
                'op': 'get',
                'attributes': ['SAI_TAM_ATTR_INT_OBJECTS_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    def test_tam_remove(self, npu):
        commands = [{'name': 'tam_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
