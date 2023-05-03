from pprint import pprint

import pytest


class TestSaiQueue:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SCHEDULER_GROUP SAI_OBJECT_TYPE_PORT

    def test_queue_create(self, npu):
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
                'name': 'scheduler_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP',
                'attributes': [
                    'SAI_SCHEDULER_GROUP_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_SCHEDULER_GROUP_ATTR_LEVEL',
                    '1',
                    'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS',
                    '1',
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
                    'SAI_QUEUE_TYPE_ALL',
                    'SAI_QUEUE_ATTR_PORT',
                    '$port_1',
                    'SAI_QUEUE_ATTR_INDEX',
                    '1',
                    'SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE',
                    '$scheduler_group_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_queue_attr_parent_scheduler_node_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': ['SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_parent_scheduler_node_set'])
    def test_sai_queue_attr_parent_scheduler_node_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_queue_attr_wred_profile_id_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': ['SAI_QUEUE_ATTR_WRED_PROFILE_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_wred_profile_id_set'])
    def test_sai_queue_attr_wred_profile_id_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_WRED_PROFILE_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_queue_attr_buffer_profile_id_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': ['SAI_QUEUE_ATTR_BUFFER_PROFILE_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_buffer_profile_id_set'])
    def test_sai_queue_attr_buffer_profile_id_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_BUFFER_PROFILE_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_queue_attr_scheduler_profile_id_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': [
                    'SAI_QUEUE_ATTR_SCHEDULER_PROFILE_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_scheduler_profile_id_set'])
    def test_sai_queue_attr_scheduler_profile_id_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_SCHEDULER_PROFILE_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_sai_queue_attr_pause_status_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_PAUSE_STATUS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_queue_attr_enable_pfc_dldr_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': ['SAI_QUEUE_ATTR_ENABLE_PFC_DLDR', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_enable_pfc_dldr_set'])
    def test_sai_queue_attr_enable_pfc_dldr_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_ENABLE_PFC_DLDR',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_queue_attr_pfc_dlr_init_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': ['SAI_QUEUE_ATTR_PFC_DLR_INIT', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_pfc_dlr_init_set'])
    def test_sai_queue_attr_pfc_dlr_init_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_PFC_DLR_INIT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_queue_attr_tam_object_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': ['SAI_QUEUE_ATTR_TAM_OBJECT', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_tam_object_set'])
    def test_sai_queue_attr_tam_object_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_TAM_OBJECT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'empty', (
            'Get error, expected empty but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_queue_attr_pfc_dlr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': [
                    'SAI_QUEUE_ATTR_PFC_DLR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_queue_attr_pfc_dlr_packet_action_set'])
    def test_sai_queue_attr_pfc_dlr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_PFC_DLR_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_PACKET_ACTION_DROP', (
            'Get error, expected SAI_PACKET_ACTION_DROP but got %s'
            % results[1][0].value()
        )

    def test_sai_queue_attr_pfc_continuous_deadlock_state_get(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'atrribute': 'SAI_QUEUE_ATTR_PFC_CONTINUOUS_DEADLOCK_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_queue_remove(self, npu):
        commands = [
            {
                'name': 'queue_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_QUEUE',
                'attributes': [
                    'SAI_QUEUE_ATTR_TYPE',
                    'SAI_QUEUE_TYPE_ALL',
                    'SAI_QUEUE_ATTR_PORT',
                    '$port_1',
                    'SAI_QUEUE_ATTR_INDEX',
                    '1',
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
                    '1',
                    'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS',
                    '1',
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
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
