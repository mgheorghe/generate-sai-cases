from pprint import pprint

import pytest


class TestSaiDtelQueueReport:
    # object with parent SAI_OBJECT_TYPE_QUEUE

    @pytest.mark.dependency(scope='session')
    def test_dtel_queue_report_create(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'scheduler_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'attributes': [
                    'SAI_SCHEDULER_GROUP_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_SCHEDULER_GROUP_ATTR_LEVEL',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE',
                    'TODO_circular parent reference',
                ],
            },
            {
                'name': 'queue_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'attributes': [
                    'SAI_QUEUE_ATTR_TYPE',
                    'sai_queue_type_t',
                    'SAI_QUEUE_ATTR_PORT',
                    '$port_1',
                    'SAI_QUEUE_ATTR_INDEX',
                    'sai_uint8_t',
                    'SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE',
                    '$scheduler_group_1',
                ],
            },
            {
                'name': 'dtel_queue_report_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DTEL_QUEUE_REPORT',
                'attributes': ['SAI_DTEL_QUEUE_REPORT_ATTR_QUEUE_ID', '$queue_1'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_dtel_queue_report_remove(self, npu):
        commands = [
            {
                'name': 'dtel_queue_report_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DTEL_QUEUE_REPORT',
                'attributes': ['SAI_DTEL_QUEUE_REPORT_ATTR_QUEUE_ID', '$queue_1'],
            },
            {
                'name': 'queue_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'attributes': [
                    'SAI_QUEUE_ATTR_TYPE',
                    'sai_queue_type_t',
                    'SAI_QUEUE_ATTR_PORT',
                    '$port_1',
                    'SAI_QUEUE_ATTR_INDEX',
                    'sai_uint8_t',
                    'SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE',
                    '$scheduler_group_1',
                ],
            },
            {
                'name': 'scheduler_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'attributes': [
                    'SAI_SCHEDULER_GROUP_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_SCHEDULER_GROUP_ATTR_LEVEL',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS',
                    'sai_uint8_t',
                    'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE',
                    'TODO_circular parent reference',
                ],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
