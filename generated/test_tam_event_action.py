from pprint import pprint

import pytest


class TestSaiTamEventAction:
    # object with parent SAI_OBJECT_TYPE_TAM_REPORT

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

    @pytest.mark.dependency(name='test_sai_tam_event_action_attr_report_type_set')
    def test_sai_tam_event_action_attr_report_type_set(self, npu):
        commands = [
            {
                'name': 'tam_event_action_1',
                'op': 'set',
                'attributes': ['SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_event_action_attr_report_type_set'])
    def test_sai_tam_event_action_attr_report_type_get(self, npu):
        commands = [
            {
                'name': 'tam_event_action_1',
                'op': 'get',
                'attributes': ['SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_event_action_attr_qos_action_type_set')
    def test_sai_tam_event_action_attr_qos_action_type_set(self, npu):
        commands = [
            {
                'name': 'tam_event_action_1',
                'op': 'set',
                'attributes': ['SAI_TAM_EVENT_ACTION_ATTR_QOS_ACTION_TYPE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_event_action_attr_qos_action_type_set']
    )
    def test_sai_tam_event_action_attr_qos_action_type_get(self, npu):
        commands = [
            {
                'name': 'tam_event_action_1',
                'op': 'get',
                'attributes': ['SAI_TAM_EVENT_ACTION_ATTR_QOS_ACTION_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_tam_event_action_remove(self, npu):
        commands = [
            {'name': 'tam_event_action_1', 'op': 'remove'},
            {'name': 'tam_report_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
