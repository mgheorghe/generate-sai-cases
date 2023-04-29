from pprint import pprint

import pytest


class TestSaiTamEvent:
    # object with parent SAI_OBJECT_TYPE_TAM_EVENT_ACTION SAI_OBJECT_TYPE_TAM_COLLECTOR

    @pytest.mark.dependency(scope='session')
    def test_tam_event_create(self, npu):
        commands = [
            {
                'name': 'tam_event_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT',
                'attributes': [
                    'SAI_TAM_EVENT_ATTR_TYPE',
                    'sai_tam_event_type_t',
                    'SAI_TAM_EVENT_ATTR_ACTION_LIST',
                    'sai_object_list_t',
                    'SAI_TAM_EVENT_ATTR_COLLECTOR_LIST',
                    'sai_object_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_tam_event_remove(self, npu):
        commands = [
            {
                'name': 'tam_event_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT',
                'attributes': [
                    'SAI_TAM_EVENT_ATTR_TYPE',
                    'sai_tam_event_type_t',
                    'SAI_TAM_EVENT_ATTR_ACTION_LIST',
                    'sai_object_list_t',
                    'SAI_TAM_EVENT_ATTR_COLLECTOR_LIST',
                    'sai_object_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
