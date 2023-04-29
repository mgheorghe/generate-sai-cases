from pprint import pprint

import pytest


class TestSaiTamEventAction:
    # object with parent SAI_OBJECT_TYPE_TAM_REPORT

    @pytest.mark.dependency(scope='session')
    def test_tam_event_action_create(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            },
            {
                'name': 'tam_event_action_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
                'attributes': [
                    'SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE',
                    '$tam_report_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tam_event_action_attr_report_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_action_attr_report_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
                'atrribute': ['SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_action_attr_report_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_action_attr_report_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
                'atrribute': 'SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_tam_event_action_attr_qos_action_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_action_attr_qos_action_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
                'atrribute': ['SAI_TAM_EVENT_ACTION_ATTR_QOS_ACTION_TYPE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_event_action_attr_qos_action_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_event_action_attr_qos_action_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
                'atrribute': 'SAI_TAM_EVENT_ACTION_ATTR_QOS_ACTION_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_tam_event_action_remove(self, npu):
        commands = [
            {
                'name': 'tam_event_action_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
                'attributes': [
                    'SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE',
                    '$tam_report_1',
                ],
            },
            {
                'name': 'tam_report_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
