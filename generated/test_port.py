from pprint import pprint

import pytest


class TestSaiPort:
    # object with no parents

    def test_port_create(self, npu):
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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_port_attr_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_oper_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_oper_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_OPER_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_breakout_mode_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_breakout_mode_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_BREAKOUT_MODE_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_current_breakout_mode_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_current_breakout_mode_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_CURRENT_BREAKOUT_MODE_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_qos_number_of_queues_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_number_of_queues_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_NUMBER_OF_QUEUES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_qos_queue_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_queue_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_QUEUE_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_qos_number_of_scheduler_groups_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_number_of_scheduler_groups_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_NUMBER_OF_SCHEDULER_GROUPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_qos_scheduler_group_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_scheduler_group_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_SCHEDULER_GROUP_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_qos_maximum_headroom_size_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_maximum_headroom_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_MAXIMUM_HEADROOM_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_fec_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_fec_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_FEC_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_fec_mode_extended_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_FEC_MODE_EXTENDED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_half_duplex_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_half_duplex_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_HALF_DUPLEX_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_auto_neg_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_AUTO_NEG_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_flow_control_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_FLOW_CONTROL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_asymmetric_pause_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_asymmetric_pause_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_ASYMMETRIC_PAUSE_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_supported_media_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_media_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_MEDIA_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_fec_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_fec_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_FEC_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_fec_mode_extended_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_FEC_MODE_EXTENDED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_half_duplex_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_half_duplex_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_HALF_DUPLEX_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_auto_neg_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_AUTO_NEG_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_flow_control_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_FLOW_CONTROL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_asymmetric_pause_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_asymmetric_pause_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_ASYMMETRIC_PAUSE_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_media_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_media_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_MEDIA_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_remote_advertised_oui_code_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_remote_advertised_oui_code_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_REMOTE_ADVERTISED_OUI_CODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_number_of_ingress_priority_groups_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_number_of_ingress_priority_groups_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_NUMBER_OF_INGRESS_PRIORITY_GROUPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_priority_group_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_priority_group_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INGRESS_PRIORITY_GROUP_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_eye_values_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_eye_values_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EYE_VALUES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_oper_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_oper_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_OPER_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_speed_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_speed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_SPEED', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_auto_neg_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_AUTO_NEG_MODE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_AUTO_NEG_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_admin_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_admin_state_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_admin_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADMIN_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_media_type_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_media_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_MEDIA_TYPE',
                    'SAI_PORT_MEDIA_TYPE_NOT_PRESENT',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_media_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_media_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MEDIA_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_MEDIA_TYPE_NOT_PRESENT' for result in results]
        ), 'Get error'

    def test_sai_port_attr_advertised_speed_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_speed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADVERTISED_SPEED', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_fec_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_fec_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADVERTISED_FEC_MODE', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_fec_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_fec_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_FEC_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_fec_mode_extended_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_fec_mode_extended_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADVERTISED_FEC_MODE_EXTENDED', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_fec_mode_extended_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_FEC_MODE_EXTENDED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_half_duplex_speed_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_half_duplex_speed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADVERTISED_HALF_DUPLEX_SPEED', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_half_duplex_speed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_half_duplex_speed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_HALF_DUPLEX_SPEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_auto_neg_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_auto_neg_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADVERTISED_AUTO_NEG_MODE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_auto_neg_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_AUTO_NEG_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_flow_control_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_flow_control_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_ADVERTISED_FLOW_CONTROL_MODE',
                    'SAI_PORT_FLOW_CONTROL_MODE_DISABLE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_flow_control_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_FLOW_CONTROL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_FLOW_CONTROL_MODE_DISABLE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_advertised_asymmetric_pause_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_asymmetric_pause_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_ADVERTISED_ASYMMETRIC_PAUSE_MODE',
                    'false',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_asymmetric_pause_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_asymmetric_pause_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_ASYMMETRIC_PAUSE_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_media_type_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_media_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_ADVERTISED_MEDIA_TYPE',
                    'SAI_PORT_MEDIA_TYPE_UNKNOWN',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_media_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_media_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_MEDIA_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_MEDIA_TYPE_UNKNOWN' for result in results]
        ), 'Get error'

    def test_sai_port_attr_advertised_oui_code_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_oui_code_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADVERTISED_OUI_CODE', '0x6A737D'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_oui_code_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_oui_code_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_OUI_CODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x6A737D' for result in results]), 'Get error'

    def test_sai_port_attr_port_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_port_vlan_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PORT_VLAN_ID', '1'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_port_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_port_vlan_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PORT_VLAN_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1' for result in results]), 'Get error'

    def test_sai_port_attr_default_vlan_priority_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_default_vlan_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_DEFAULT_VLAN_PRIORITY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_default_vlan_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_default_vlan_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_DEFAULT_VLAN_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_drop_untagged_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_drop_untagged_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_DROP_UNTAGGED', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_drop_untagged_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_drop_untagged_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_DROP_UNTAGGED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_drop_tagged_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_drop_tagged_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_DROP_TAGGED', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_drop_tagged_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_drop_tagged_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_DROP_TAGGED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_internal_loopback_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_internal_loopback_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_INTERNAL_LOOPBACK_MODE',
                    'SAI_PORT_INTERNAL_LOOPBACK_MODE_NONE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_internal_loopback_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_internal_loopback_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INTERNAL_LOOPBACK_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_INTERNAL_LOOPBACK_MODE_NONE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_use_extended_fec_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_use_extended_fec_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_USE_EXTENDED_FEC', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_use_extended_fec_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_use_extended_fec_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_USE_EXTENDED_FEC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_fec_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fec_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_FEC_MODE', 'SAI_PORT_FEC_MODE_NONE'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_fec_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fec_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FEC_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_FEC_MODE_NONE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_fec_mode_extended_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fec_mode_extended_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_FEC_MODE_EXTENDED',
                    'SAI_PORT_FEC_MODE_EXTENDED_NONE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fec_mode_extended_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FEC_MODE_EXTENDED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_FEC_MODE_EXTENDED_NONE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_update_dscp_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_update_dscp_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_UPDATE_DSCP', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_update_dscp_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_update_dscp_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_UPDATE_DSCP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_mtu_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_mtu_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_MTU', '1514'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_mtu_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_mtu_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MTU',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1514' for result in results]), 'Get error'

    def test_sai_port_attr_flood_storm_control_policer_id_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_flood_storm_control_policer_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_FLOOD_STORM_CONTROL_POLICER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_flood_storm_control_policer_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_flood_storm_control_policer_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FLOOD_STORM_CONTROL_POLICER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_broadcast_storm_control_policer_id_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_broadcast_storm_control_policer_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_BROADCAST_STORM_CONTROL_POLICER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_broadcast_storm_control_policer_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_broadcast_storm_control_policer_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_BROADCAST_STORM_CONTROL_POLICER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_multicast_storm_control_policer_id_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_multicast_storm_control_policer_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_MULTICAST_STORM_CONTROL_POLICER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_multicast_storm_control_policer_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_multicast_storm_control_policer_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MULTICAST_STORM_CONTROL_POLICER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_global_flow_control_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_global_flow_control_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_MODE',
                    'SAI_PORT_FLOW_CONTROL_MODE_DISABLE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_global_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_global_flow_control_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_FLOW_CONTROL_MODE_DISABLE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_egress_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_egress_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EGRESS_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_macsec_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_macsec_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_INGRESS_MACSEC_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_macsec_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_macsec_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INGRESS_MACSEC_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_egress_macsec_acl_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_macsec_acl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EGRESS_MACSEC_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_egress_macsec_acl_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_macsec_acl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EGRESS_MACSEC_ACL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_macsec_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_macsec_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MACSEC_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_mirror_session_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_INGRESS_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_mirror_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INGRESS_MIRROR_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_egress_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_mirror_session_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EGRESS_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_egress_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_mirror_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EGRESS_MIRROR_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_samplepacket_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_INGRESS_SAMPLEPACKET_ENABLE',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_samplepacket_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INGRESS_SAMPLEPACKET_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_egress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_samplepacket_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_EGRESS_SAMPLEPACKET_ENABLE',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_egress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_samplepacket_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EGRESS_SAMPLEPACKET_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_sample_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_sample_mirror_session_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_INGRESS_SAMPLE_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ingress_sample_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ingress_sample_mirror_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INGRESS_SAMPLE_MIRROR_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_egress_sample_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_sample_mirror_session_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EGRESS_SAMPLE_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_egress_sample_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_sample_mirror_session_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EGRESS_SAMPLE_MIRROR_SESSION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_policer_id_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_policer_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_POLICER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_policer_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_policer_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_POLICER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_default_tc_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_default_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_QOS_DEFAULT_TC', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_default_tc_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_default_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_DEFAULT_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dot1p_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dot1p_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_DOT1P_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dot1p_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dot1p_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_DOT1P_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dot1p_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dot1p_to_color_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_DOT1P_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dot1p_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dot1p_to_color_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_DOT1P_TO_COLOR_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dscp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dscp_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_QOS_DSCP_TO_TC_MAP', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dscp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dscp_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_DSCP_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dscp_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dscp_to_color_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_DSCP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dscp_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dscp_to_color_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_DSCP_TO_COLOR_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_to_queue_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_TC_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_to_queue_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_TC_TO_QUEUE_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_and_color_to_dot1p_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_and_color_to_dot1p_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DOT1P_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_and_color_to_dot1p_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_and_color_to_dot1p_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DOT1P_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_and_color_to_dscp_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_and_color_to_dscp_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DSCP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_and_color_to_dscp_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_and_color_to_dscp_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DSCP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_to_priority_group_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_to_priority_group_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_TC_TO_PRIORITY_GROUP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_to_priority_group_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_to_priority_group_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_TC_TO_PRIORITY_GROUP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_pfc_priority_to_priority_group_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_pfc_priority_to_priority_group_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_PRIORITY_GROUP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_pfc_priority_to_priority_group_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_pfc_priority_to_priority_group_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_PRIORITY_GROUP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_pfc_priority_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_pfc_priority_to_queue_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_pfc_priority_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_pfc_priority_to_queue_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_QUEUE_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_scheduler_profile_id_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_scheduler_profile_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_SCHEDULER_PROFILE_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_scheduler_profile_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_scheduler_profile_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_SCHEDULER_PROFILE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_ingress_buffer_profile_list_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_ingress_buffer_profile_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_QOS_INGRESS_BUFFER_PROFILE_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_ingress_buffer_profile_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_ingress_buffer_profile_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_INGRESS_BUFFER_PROFILE_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_qos_egress_buffer_profile_list_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_egress_buffer_profile_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_QOS_EGRESS_BUFFER_PROFILE_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_egress_buffer_profile_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_egress_buffer_profile_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_EGRESS_BUFFER_PROFILE_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_MODE',
                    'SAI_PORT_PRIORITY_FLOW_CONTROL_MODE_COMBINED',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'SAI_PORT_PRIORITY_FLOW_CONTROL_MODE_COMBINED'
                for result in results
            ]
        ), 'Get error'

    def test_sai_port_attr_priority_flow_control_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_rx_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_rx_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_RX', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_rx_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_rx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_RX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_tx_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_tx_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_TX', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_tx_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_tx_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_TX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_meta_data_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_META_DATA', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_meta_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_META_DATA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_egress_block_port_list_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_block_port_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EGRESS_BLOCK_PORT_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_egress_block_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_egress_block_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EGRESS_BLOCK_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_hw_profile_id_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_hw_profile_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_HW_PROFILE_ID', 'vendor'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_hw_profile_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_hw_profile_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_HW_PROFILE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'vendor' for result in results]), 'Get error'

    def test_sai_port_attr_eee_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_eee_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EEE_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_eee_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_eee_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EEE_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_eee_idle_time_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_eee_idle_time_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EEE_IDLE_TIME', '2500'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_eee_idle_time_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_eee_idle_time_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EEE_IDLE_TIME',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '2500' for result in results]), 'Get error'

    def test_sai_port_attr_eee_wake_time_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_eee_wake_time_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_EEE_WAKE_TIME', '5'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_eee_wake_time_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_eee_wake_time_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_EEE_WAKE_TIME',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '5' for result in results]), 'Get error'

    def test_sai_port_attr_port_pool_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_port_pool_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PORT_POOL_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_isolation_group_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_isolation_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ISOLATION_GROUP', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_isolation_group_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_isolation_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ISOLATION_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_pkt_tx_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pkt_tx_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PKT_TX_ENABLE', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_pkt_tx_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pkt_tx_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PKT_TX_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_port_attr_tam_object_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_tam_object_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_TAM_OBJECT', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_tam_object_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_tam_object_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_TAM_OBJECT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_serdes_preemphasis_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_serdes_preemphasis_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_SERDES_PREEMPHASIS', 'internal'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_serdes_preemphasis_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_serdes_preemphasis_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SERDES_PREEMPHASIS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_port_attr_serdes_idriver_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_serdes_idriver_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_SERDES_IDRIVER', 'internal'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_serdes_idriver_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_serdes_idriver_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SERDES_IDRIVER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_port_attr_serdes_ipredriver_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_serdes_ipredriver_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_SERDES_IPREDRIVER', 'internal'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_serdes_ipredriver_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_serdes_ipredriver_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SERDES_IPREDRIVER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_port_attr_link_training_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_link_training_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_LINK_TRAINING_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_link_training_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_link_training_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_LINK_TRAINING_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_ptp_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ptp_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PTP_MODE', 'SAI_PORT_PTP_MODE_NONE'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ptp_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ptp_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PTP_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_PTP_MODE_NONE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_interface_type_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_interface_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_INTERFACE_TYPE',
                    'SAI_PORT_INTERFACE_TYPE_NONE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_interface_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_interface_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_INTERFACE_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_INTERFACE_TYPE_NONE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_advertised_interface_type_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_interface_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ADVERTISED_INTERFACE_TYPE', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_advertised_interface_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_advertised_interface_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ADVERTISED_INTERFACE_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_prbs_polynomial_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_polynomial_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PRBS_POLYNOMIAL', 'internal'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_prbs_polynomial_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_polynomial_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRBS_POLYNOMIAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_port_attr_port_serdes_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_port_serdes_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PORT_SERDES_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'internal' for result in results]), 'Get error'

    def test_sai_port_attr_link_training_failure_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_link_training_failure_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_LINK_TRAINING_FAILURE_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_link_training_rx_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_link_training_rx_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_LINK_TRAINING_RX_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_prbs_config_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_config_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_PRBS_CONFIG',
                    'SAI_PORT_PRBS_CONFIG_DISABLE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_prbs_config_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_config_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRBS_CONFIG',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_PRBS_CONFIG_DISABLE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_prbs_lock_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_lock_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRBS_LOCK_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_prbs_lock_loss_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_lock_loss_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRBS_LOCK_LOSS_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_prbs_rx_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_rx_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRBS_RX_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_prbs_rx_state_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_prbs_rx_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRBS_RX_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_auto_neg_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_AUTO_NEG_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_disable_decrement_ttl_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_disable_decrement_ttl_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_DISABLE_DECREMENT_TTL', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_disable_decrement_ttl_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_disable_decrement_ttl_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_DISABLE_DECREMENT_TTL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_qos_mpls_exp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_mpls_exp_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_mpls_exp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_mpls_exp_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_mpls_exp_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_mpls_exp_to_color_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_mpls_exp_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_mpls_exp_to_color_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_COLOR_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_and_color_to_mpls_exp_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_and_color_to_mpls_exp_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_tc_and_color_to_mpls_exp_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_tc_and_color_to_mpls_exp_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_tpid_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_tpid_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_TPID', '0x8100'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_tpid_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_tpid_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_TPID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0x8100' for result in results]), 'Get error'

    def test_sai_port_attr_err_status_list_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_err_status_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ERR_STATUS_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_fabric_attached_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fabric_attached_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FABRIC_ATTACHED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_fabric_attached_switch_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fabric_attached_switch_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FABRIC_ATTACHED_SWITCH_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_fabric_attached_switch_id_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fabric_attached_switch_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FABRIC_ATTACHED_SWITCH_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_fabric_attached_port_index_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fabric_attached_port_index_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FABRIC_ATTACHED_PORT_INDEX',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_fabric_reachability_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fabric_reachability_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FABRIC_REACHABILITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_system_port_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_system_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SYSTEM_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_auto_neg_fec_mode_override_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_fec_mode_override_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_AUTO_NEG_FEC_MODE_OVERRIDE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_auto_neg_fec_mode_override_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_fec_mode_override_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_AUTO_NEG_FEC_MODE_OVERRIDE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_loopback_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_loopback_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_LOOPBACK_MODE',
                    'SAI_PORT_LOOPBACK_MODE_NONE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_loopback_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_loopback_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_LOOPBACK_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_LOOPBACK_MODE_NONE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_mdix_mode_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_mdix_mode_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MDIX_MODE_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_mdix_mode_config_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_mdix_mode_config_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_MDIX_MODE_CONFIG',
                    'SAI_PORT_MDIX_MODE_CONFIG_AUTO',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_mdix_mode_config_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_mdix_mode_config_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MDIX_MODE_CONFIG',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_MDIX_MODE_CONFIG_AUTO' for result in results]
        ), 'Get error'

    def test_sai_port_attr_auto_neg_config_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_config_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_AUTO_NEG_CONFIG_MODE',
                    'SAI_PORT_AUTO_NEG_CONFIG_MODE_DISABLED',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_auto_neg_config_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_config_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_AUTO_NEG_CONFIG_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_AUTO_NEG_CONFIG_MODE_DISABLED' for result in results]
        ), 'Get error'

    def test_sai_port_attr_1000x_sgmii_slave_autodetect_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_1000x_sgmii_slave_autodetect_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_1000X_SGMII_SLAVE_AUTODETECT', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_1000x_sgmii_slave_autodetect_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_1000x_sgmii_slave_autodetect_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_1000X_SGMII_SLAVE_AUTODETECT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_module_type_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_module_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_MODULE_TYPE',
                    'SAI_PORT_MODULE_TYPE_1000BASE_X',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_module_type_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_module_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MODULE_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_MODULE_TYPE_1000BASE_X' for result in results]
        ), 'Get error'

    def test_sai_port_attr_dual_media_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_dual_media_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_DUAL_MEDIA', 'SAI_PORT_DUAL_MEDIA_NONE'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_dual_media_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_dual_media_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_DUAL_MEDIA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_DUAL_MEDIA_NONE' for result in results]
        ), 'Get error'

    def test_sai_port_attr_auto_neg_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_auto_neg_fec_mode_extended_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_AUTO_NEG_FEC_MODE_EXTENDED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_ipg_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ipg_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_IPG', '96'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ipg_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ipg_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_IPG',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '96' for result in results]), 'Get error'

    def test_sai_port_attr_global_flow_control_forward_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_global_flow_control_forward_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_FORWARD', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_global_flow_control_forward_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_global_flow_control_forward_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_FORWARD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_forward_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_forward_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_FORWARD', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_priority_flow_control_forward_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_priority_flow_control_forward_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_FORWARD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dscp_to_forwarding_class_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dscp_to_forwarding_class_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_DSCP_TO_FORWARDING_CLASS_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_dscp_to_forwarding_class_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_dscp_to_forwarding_class_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_DSCP_TO_FORWARDING_CLASS_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_qos_mpls_exp_to_forwarding_class_map_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_mpls_exp_to_forwarding_class_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_FORWARDING_CLASS_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_qos_mpls_exp_to_forwarding_class_map_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_qos_mpls_exp_to_forwarding_class_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_FORWARDING_CLASS_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_port_attr_ipsec_port_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ipsec_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_IPSEC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_pfc_tc_dld_interval_range_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pfc_tc_dld_interval_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PFC_TC_DLD_INTERVAL_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_pfc_tc_dld_interval_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pfc_tc_dld_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PFC_TC_DLD_INTERVAL', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_pfc_tc_dld_interval_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pfc_tc_dld_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PFC_TC_DLD_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_pfc_tc_dlr_interval_range_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pfc_tc_dlr_interval_range_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PFC_TC_DLR_INTERVAL_RANGE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_pfc_tc_dlr_interval_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pfc_tc_dlr_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_PFC_TC_DLR_INTERVAL', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_pfc_tc_dlr_interval_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pfc_tc_dlr_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PFC_TC_DLR_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_port_attr_supported_link_training_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_supported_link_training_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_SUPPORTED_LINK_TRAINING_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_rx_signal_detect_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_rx_signal_detect_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_RX_SIGNAL_DETECT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_rx_lock_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_rx_lock_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_RX_LOCK_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_pcs_rx_link_status_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_pcs_rx_link_status_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_PCS_RX_LINK_STATUS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_fec_alignment_lock_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fec_alignment_lock_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FEC_ALIGNMENT_LOCK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_fabric_isolate_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fabric_isolate_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_FABRIC_ISOLATE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_fabric_isolate_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_fabric_isolate_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_FABRIC_ISOLATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_max_fec_symbol_errors_detectable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_max_fec_symbol_errors_detectable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_MAX_FEC_SYMBOL_ERRORS_DETECTABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_ars_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ARS_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ars_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ARS_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_ars_port_load_scaling_factor_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_port_load_scaling_factor_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ARS_PORT_LOAD_SCALING_FACTOR', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ars_port_load_scaling_factor_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_port_load_scaling_factor_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ARS_PORT_LOAD_SCALING_FACTOR',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_ars_port_load_past_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_port_load_past_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ARS_PORT_LOAD_PAST_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ars_port_load_past_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_port_load_past_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ARS_PORT_LOAD_PAST_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_ars_port_load_future_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_port_load_future_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ARS_PORT_LOAD_FUTURE_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ars_port_load_future_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_port_load_future_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ARS_PORT_LOAD_FUTURE_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_ars_alternate_path_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_alternate_path_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ARS_ALTERNATE_PATH', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ars_alternate_path_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ars_alternate_path_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ARS_ALTERNATE_PATH',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_port_attr_json_formatted_debug_data_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_json_formatted_debug_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_JSON_FORMATTED_DEBUG_DATA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_port_attr_ecmp_hash_algorithm_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ecmp_hash_algorithm_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': [
                    'SAI_PORT_ATTR_ECMP_HASH_ALGORITHM',
                    'SAI_HASH_ALGORITHM_CRC',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ecmp_hash_algorithm_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ecmp_hash_algorithm_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ECMP_HASH_ALGORITHM',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_HASH_ALGORITHM_CRC' for result in results]
        ), 'Get error'

    def test_sai_port_attr_ecmp_hash_seed_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ecmp_hash_seed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ECMP_HASH_SEED', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ecmp_hash_seed_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ecmp_hash_seed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ECMP_HASH_SEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_port_attr_ecmp_hash_offset_set(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ecmp_hash_offset_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': ['SAI_PORT_ATTR_ECMP_HASH_OFFSET', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_attr_ecmp_hash_offset_get(self, npu):
        commands = [
            {
                'name': 'sai_port_attr_ecmp_hash_offset_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'atrribute': 'SAI_PORT_ATTR_ECMP_HASH_OFFSET',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_port_remove(self, npu):
        commands = [
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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
