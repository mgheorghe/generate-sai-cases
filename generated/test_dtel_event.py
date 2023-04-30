from pprint import pprint

import pytest


class TestSaiDtelEvent:
    # object with no parents

    def test_dtel_event_create(self, npu):
        commands = [
            {
                'name': 'dtel_event_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DTEL_EVENT',
                'attributes': [
                    'SAI_DTEL_EVENT_ATTR_TYPE',
                    'SAI_DTEL_EVENT_TYPE_FLOW_STATE',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_dtel_event_attr_report_session_set(self, npu):
        commands = [
            {
                'name': 'sai_dtel_event_attr_report_session_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_EVENT',
                'atrribute': [
                    'SAI_DTEL_EVENT_ATTR_REPORT_SESSION',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dtel_event_attr_report_session_get(self, npu):
        commands = [
            {
                'name': 'sai_dtel_event_attr_report_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_EVENT',
                'atrribute': 'SAI_DTEL_EVENT_ATTR_REPORT_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_dtel_event_attr_dscp_value_set(self, npu):
        commands = [
            {
                'name': 'sai_dtel_event_attr_dscp_value_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_EVENT',
                'atrribute': ['SAI_DTEL_EVENT_ATTR_DSCP_VALUE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dtel_event_attr_dscp_value_get(self, npu):
        commands = [
            {
                'name': 'sai_dtel_event_attr_dscp_value_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_EVENT',
                'atrribute': 'SAI_DTEL_EVENT_ATTR_DSCP_VALUE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_dtel_event_remove(self, npu):
        commands = [
            {
                'name': 'dtel_event_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DTEL_EVENT',
                'attributes': [
                    'SAI_DTEL_EVENT_ATTR_TYPE',
                    'SAI_DTEL_EVENT_TYPE_FLOW_STATE',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
