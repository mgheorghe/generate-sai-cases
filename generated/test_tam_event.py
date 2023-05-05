from pprint import pprint

import pytest


class TestSaiTamEvent:
    # object with parent SAI_OBJECT_TYPE_TAM_EVENT_ACTION SAI_OBJECT_TYPE_TAM_COLLECTOR

    def test_tam_event_create(self, npu):
        commands = [
            {
                'name': 'tam_event_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT',
                'attributes': [
                    'SAI_TAM_EVENT_ATTR_TYPE',
                    'SAI_TAM_EVENT_TYPE_FLOW_STATE',
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

    @pytest.mark.dependency(name='test_sai_tam_event_attr_threshold_set')
    def test_sai_tam_event_attr_threshold_set(self, npu):
        commands = [
            {
                'name': 'tam_event_1',
                'op': 'set',
                'attributes': ['SAI_TAM_EVENT_ATTR_THRESHOLD', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_event_attr_threshold_set'])
    def test_sai_tam_event_attr_threshold_get(self, npu):
        commands = [
            {
                'name': 'tam_event_1',
                'op': 'get',
                'attributes': ['SAI_TAM_EVENT_ATTR_THRESHOLD'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_tam_event_attr_dscp_value_set')
    def test_sai_tam_event_attr_dscp_value_set(self, npu):
        commands = [
            {
                'name': 'tam_event_1',
                'op': 'set',
                'attributes': ['SAI_TAM_EVENT_ATTR_DSCP_VALUE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_event_attr_dscp_value_set'])
    def test_sai_tam_event_attr_dscp_value_get(self, npu):
        commands = [
            {
                'name': 'tam_event_1',
                'op': 'get',
                'attributes': ['SAI_TAM_EVENT_ATTR_DSCP_VALUE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_tam_event_remove(self, npu):
        commands = [{'name': 'tam_event_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
