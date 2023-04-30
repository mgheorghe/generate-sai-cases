from pprint import pprint

import pytest


class TestSaiPolicer:
    # object with no parents

    def test_policer_create(self, npu):
        commands = [
            {
                'name': 'policer_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'attributes': [
                    'SAI_POLICER_ATTR_METER_TYPE',
                    'SAI_METER_TYPE_PACKETS',
                    'SAI_POLICER_ATTR_MODE',
                    'SAI_POLICER_MODE_SR_TCM',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_policer_attr_cbs_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_cbs_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': ['SAI_POLICER_ATTR_CBS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_cbs_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_cbs_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_CBS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_policer_attr_cir_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_cir_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': ['SAI_POLICER_ATTR_CIR', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_cir_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_cir_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_CIR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_policer_attr_pbs_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_pbs_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': ['SAI_POLICER_ATTR_PBS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_pbs_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_pbs_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_PBS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_policer_attr_pir_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_pir_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': ['SAI_POLICER_ATTR_PIR', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_pir_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_pir_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_PIR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_policer_attr_green_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_green_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': [
                    'SAI_POLICER_ATTR_GREEN_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_green_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_green_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_GREEN_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_policer_attr_yellow_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_yellow_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': [
                    'SAI_POLICER_ATTR_YELLOW_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_yellow_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_yellow_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_YELLOW_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_policer_attr_red_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_red_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': [
                    'SAI_POLICER_ATTR_RED_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_red_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_red_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_RED_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_policer_attr_enable_counter_packet_action_list_set(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_enable_counter_packet_action_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': [
                    'SAI_POLICER_ATTR_ENABLE_COUNTER_PACKET_ACTION_LIST',
                    'empty',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_policer_attr_enable_counter_packet_action_list_get(self, npu):
        commands = [
            {
                'name': 'sai_policer_attr_enable_counter_packet_action_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'atrribute': 'SAI_POLICER_ATTR_ENABLE_COUNTER_PACKET_ACTION_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_policer_remove(self, npu):
        commands = [
            {
                'name': 'policer_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'attributes': [
                    'SAI_POLICER_ATTR_METER_TYPE',
                    'SAI_METER_TYPE_PACKETS',
                    'SAI_POLICER_ATTR_MODE',
                    'SAI_POLICER_MODE_SR_TCM',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
