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
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_TYPE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_oper_status_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_OPER_STATUS']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_breakout_mode_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_BREAKOUT_MODE_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_current_breakout_mode_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_CURRENT_BREAKOUT_MODE_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_qos_number_of_queues_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_NUMBER_OF_QUEUES'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_qos_queue_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_QUEUE_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_qos_number_of_scheduler_groups_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_NUMBER_OF_SCHEDULER_GROUPS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_qos_scheduler_group_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_SCHEDULER_GROUP_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_qos_maximum_headroom_size_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_MAXIMUM_HEADROOM_SIZE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_speed_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_SPEED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_fec_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_FEC_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_FEC_MODE_EXTENDED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_half_duplex_speed_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_HALF_DUPLEX_SPEED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_AUTO_NEG_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_FLOW_CONTROL_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_asymmetric_pause_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_ASYMMETRIC_PAUSE_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_supported_media_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_MEDIA_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_speed_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_SPEED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_fec_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_FEC_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_FEC_MODE_EXTENDED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_half_duplex_speed_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_HALF_DUPLEX_SPEED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_AUTO_NEG_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_FLOW_CONTROL_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_asymmetric_pause_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_ASYMMETRIC_PAUSE_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_media_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_MEDIA_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_remote_advertised_oui_code_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_REMOTE_ADVERTISED_OUI_CODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_number_of_ingress_priority_groups_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_NUMBER_OF_INGRESS_PRIORITY_GROUPS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_ingress_priority_group_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_INGRESS_PRIORITY_GROUP_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_eye_values_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_EYE_VALUES']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_oper_speed_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_OPER_SPEED']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_speed_set')
    def test_sai_port_attr_speed_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_SPEED', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_speed_set'])
    def test_sai_port_attr_speed_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_SPEED']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_auto_neg_mode_set')
    def test_sai_port_attr_auto_neg_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_AUTO_NEG_MODE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_auto_neg_mode_set'])
    def test_sai_port_attr_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_AUTO_NEG_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_admin_state_set')
    def test_sai_port_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_admin_state_set'])
    def test_sai_port_attr_admin_state_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_ADMIN_STATE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_media_type_set')
    def test_sai_port_attr_media_type_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_MEDIA_TYPE',
                    'SAI_PORT_MEDIA_TYPE_NOT_PRESENT',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_media_type_set'])
    def test_sai_port_attr_media_type_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_MEDIA_TYPE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_MEDIA_TYPE_NOT_PRESENT', (
            'Get error, expected SAI_PORT_MEDIA_TYPE_NOT_PRESENT but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_speed_set')
    def test_sai_port_attr_advertised_speed_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_SPEED', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_advertised_speed_set'])
    def test_sai_port_attr_advertised_speed_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_SPEED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_fec_mode_set')
    def test_sai_port_attr_advertised_fec_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_FEC_MODE', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_advertised_fec_mode_set'])
    def test_sai_port_attr_advertised_fec_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_FEC_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_fec_mode_extended_set')
    def test_sai_port_attr_advertised_fec_mode_extended_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_FEC_MODE_EXTENDED', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_advertised_fec_mode_extended_set']
    )
    def test_sai_port_attr_advertised_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_FEC_MODE_EXTENDED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_half_duplex_speed_set')
    def test_sai_port_attr_advertised_half_duplex_speed_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_HALF_DUPLEX_SPEED', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_advertised_half_duplex_speed_set']
    )
    def test_sai_port_attr_advertised_half_duplex_speed_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_HALF_DUPLEX_SPEED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_auto_neg_mode_set')
    def test_sai_port_attr_advertised_auto_neg_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_AUTO_NEG_MODE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_advertised_auto_neg_mode_set'])
    def test_sai_port_attr_advertised_auto_neg_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_AUTO_NEG_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_flow_control_mode_set')
    def test_sai_port_attr_advertised_flow_control_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_ADVERTISED_FLOW_CONTROL_MODE',
                    'SAI_PORT_FLOW_CONTROL_MODE_DISABLE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_advertised_flow_control_mode_set']
    )
    def test_sai_port_attr_advertised_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_FLOW_CONTROL_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_FLOW_CONTROL_MODE_DISABLE', (
            'Get error, expected SAI_PORT_FLOW_CONTROL_MODE_DISABLE but got %s'
            % r_value
        )

    @pytest.mark.dependency(
        name='test_sai_port_attr_advertised_asymmetric_pause_mode_set'
    )
    def test_sai_port_attr_advertised_asymmetric_pause_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_ADVERTISED_ASYMMETRIC_PAUSE_MODE',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_advertised_asymmetric_pause_mode_set']
    )
    def test_sai_port_attr_advertised_asymmetric_pause_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_ASYMMETRIC_PAUSE_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_media_type_set')
    def test_sai_port_attr_advertised_media_type_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_ADVERTISED_MEDIA_TYPE',
                    'SAI_PORT_MEDIA_TYPE_UNKNOWN',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_advertised_media_type_set'])
    def test_sai_port_attr_advertised_media_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_MEDIA_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_MEDIA_TYPE_UNKNOWN', (
            'Get error, expected SAI_PORT_MEDIA_TYPE_UNKNOWN but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_oui_code_set')
    def test_sai_port_attr_advertised_oui_code_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_OUI_CODE', '0x6A737D'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_advertised_oui_code_set'])
    def test_sai_port_attr_advertised_oui_code_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_OUI_CODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0x6A737D', (
            'Get error, expected 0x6A737D but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_port_vlan_id_set')
    def test_sai_port_attr_port_vlan_id_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PORT_VLAN_ID', '1'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_port_vlan_id_set'])
    def test_sai_port_attr_port_vlan_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PORT_VLAN_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '1', 'Get error, expected 1 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_default_vlan_priority_set')
    def test_sai_port_attr_default_vlan_priority_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_DEFAULT_VLAN_PRIORITY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_default_vlan_priority_set'])
    def test_sai_port_attr_default_vlan_priority_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_DEFAULT_VLAN_PRIORITY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_drop_untagged_set')
    def test_sai_port_attr_drop_untagged_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_DROP_UNTAGGED', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_drop_untagged_set'])
    def test_sai_port_attr_drop_untagged_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_DROP_UNTAGGED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_drop_tagged_set')
    def test_sai_port_attr_drop_tagged_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_DROP_TAGGED', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_drop_tagged_set'])
    def test_sai_port_attr_drop_tagged_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_DROP_TAGGED']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_internal_loopback_mode_set')
    def test_sai_port_attr_internal_loopback_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_INTERNAL_LOOPBACK_MODE',
                    'SAI_PORT_INTERNAL_LOOPBACK_MODE_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_internal_loopback_mode_set'])
    def test_sai_port_attr_internal_loopback_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_INTERNAL_LOOPBACK_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_INTERNAL_LOOPBACK_MODE_NONE', (
            'Get error, expected SAI_PORT_INTERNAL_LOOPBACK_MODE_NONE but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_use_extended_fec_set')
    def test_sai_port_attr_use_extended_fec_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_USE_EXTENDED_FEC', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_use_extended_fec_set'])
    def test_sai_port_attr_use_extended_fec_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_USE_EXTENDED_FEC'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_fec_mode_set')
    def test_sai_port_attr_fec_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_FEC_MODE', 'SAI_PORT_FEC_MODE_NONE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_fec_mode_set'])
    def test_sai_port_attr_fec_mode_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_FEC_MODE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_FEC_MODE_NONE', (
            'Get error, expected SAI_PORT_FEC_MODE_NONE but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_fec_mode_extended_set')
    def test_sai_port_attr_fec_mode_extended_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_FEC_MODE_EXTENDED',
                    'SAI_PORT_FEC_MODE_EXTENDED_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_fec_mode_extended_set'])
    def test_sai_port_attr_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FEC_MODE_EXTENDED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_FEC_MODE_EXTENDED_NONE', (
            'Get error, expected SAI_PORT_FEC_MODE_EXTENDED_NONE but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_update_dscp_set')
    def test_sai_port_attr_update_dscp_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_UPDATE_DSCP', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_update_dscp_set'])
    def test_sai_port_attr_update_dscp_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_UPDATE_DSCP']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_mtu_set')
    def test_sai_port_attr_mtu_set(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'set', 'attributes': ['SAI_PORT_ATTR_MTU', '1514']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_mtu_set'])
    def test_sai_port_attr_mtu_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_MTU']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '1514', 'Get error, expected 1514 but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_port_attr_flood_storm_control_policer_id_set'
    )
    def test_sai_port_attr_flood_storm_control_policer_id_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_FLOOD_STORM_CONTROL_POLICER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_flood_storm_control_policer_id_set']
    )
    def test_sai_port_attr_flood_storm_control_policer_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FLOOD_STORM_CONTROL_POLICER_ID'],
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

    @pytest.mark.dependency(
        name='test_sai_port_attr_broadcast_storm_control_policer_id_set'
    )
    def test_sai_port_attr_broadcast_storm_control_policer_id_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_BROADCAST_STORM_CONTROL_POLICER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_broadcast_storm_control_policer_id_set']
    )
    def test_sai_port_attr_broadcast_storm_control_policer_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_BROADCAST_STORM_CONTROL_POLICER_ID'],
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

    @pytest.mark.dependency(
        name='test_sai_port_attr_multicast_storm_control_policer_id_set'
    )
    def test_sai_port_attr_multicast_storm_control_policer_id_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_MULTICAST_STORM_CONTROL_POLICER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_multicast_storm_control_policer_id_set']
    )
    def test_sai_port_attr_multicast_storm_control_policer_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_MULTICAST_STORM_CONTROL_POLICER_ID'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_global_flow_control_mode_set')
    def test_sai_port_attr_global_flow_control_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_MODE',
                    'SAI_PORT_FLOW_CONTROL_MODE_DISABLE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_global_flow_control_mode_set'])
    def test_sai_port_attr_global_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_FLOW_CONTROL_MODE_DISABLE', (
            'Get error, expected SAI_PORT_FLOW_CONTROL_MODE_DISABLE but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_ingress_acl_set')
    def test_sai_port_attr_ingress_acl_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_INGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ingress_acl_set'])
    def test_sai_port_attr_ingress_acl_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_INGRESS_ACL']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_egress_acl_set')
    def test_sai_port_attr_egress_acl_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EGRESS_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_egress_acl_set'])
    def test_sai_port_attr_egress_acl_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_EGRESS_ACL']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_ingress_macsec_acl_set')
    def test_sai_port_attr_ingress_macsec_acl_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_INGRESS_MACSEC_ACL',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ingress_macsec_acl_set'])
    def test_sai_port_attr_ingress_macsec_acl_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_INGRESS_MACSEC_ACL'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_egress_macsec_acl_set')
    def test_sai_port_attr_egress_macsec_acl_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EGRESS_MACSEC_ACL', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_egress_macsec_acl_set'])
    def test_sai_port_attr_egress_macsec_acl_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_EGRESS_MACSEC_ACL'],
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

    def test_sai_port_attr_macsec_port_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_MACSEC_PORT_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ingress_mirror_session_set')
    def test_sai_port_attr_ingress_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_INGRESS_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ingress_mirror_session_set'])
    def test_sai_port_attr_ingress_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_INGRESS_MIRROR_SESSION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_egress_mirror_session_set')
    def test_sai_port_attr_egress_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EGRESS_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_egress_mirror_session_set'])
    def test_sai_port_attr_egress_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_EGRESS_MIRROR_SESSION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ingress_samplepacket_enable_set')
    def test_sai_port_attr_ingress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_INGRESS_SAMPLEPACKET_ENABLE',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_ingress_samplepacket_enable_set']
    )
    def test_sai_port_attr_ingress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_INGRESS_SAMPLEPACKET_ENABLE'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_egress_samplepacket_enable_set')
    def test_sai_port_attr_egress_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_EGRESS_SAMPLEPACKET_ENABLE',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_egress_samplepacket_enable_set']
    )
    def test_sai_port_attr_egress_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_EGRESS_SAMPLEPACKET_ENABLE'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_ingress_sample_mirror_session_set')
    def test_sai_port_attr_ingress_sample_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_INGRESS_SAMPLE_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_ingress_sample_mirror_session_set']
    )
    def test_sai_port_attr_ingress_sample_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_INGRESS_SAMPLE_MIRROR_SESSION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_egress_sample_mirror_session_set')
    def test_sai_port_attr_egress_sample_mirror_session_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EGRESS_SAMPLE_MIRROR_SESSION', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_egress_sample_mirror_session_set']
    )
    def test_sai_port_attr_egress_sample_mirror_session_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_EGRESS_SAMPLE_MIRROR_SESSION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_policer_id_set')
    def test_sai_port_attr_policer_id_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_POLICER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_policer_id_set'])
    def test_sai_port_attr_policer_id_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_POLICER_ID']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_qos_default_tc_set')
    def test_sai_port_attr_qos_default_tc_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_QOS_DEFAULT_TC', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_default_tc_set'])
    def test_sai_port_attr_qos_default_tc_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_DEFAULT_TC'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_qos_dot1p_to_tc_map_set')
    def test_sai_port_attr_qos_dot1p_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_DOT1P_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_dot1p_to_tc_map_set'])
    def test_sai_port_attr_qos_dot1p_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_DOT1P_TO_TC_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_dot1p_to_color_map_set')
    def test_sai_port_attr_qos_dot1p_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_DOT1P_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_dot1p_to_color_map_set'])
    def test_sai_port_attr_qos_dot1p_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_DOT1P_TO_COLOR_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_dscp_to_tc_map_set')
    def test_sai_port_attr_qos_dscp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_DSCP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_dscp_to_tc_map_set'])
    def test_sai_port_attr_qos_dscp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_DSCP_TO_TC_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_dscp_to_color_map_set')
    def test_sai_port_attr_qos_dscp_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_DSCP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_dscp_to_color_map_set'])
    def test_sai_port_attr_qos_dscp_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_DSCP_TO_COLOR_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_tc_to_queue_map_set')
    def test_sai_port_attr_qos_tc_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_TC_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_tc_to_queue_map_set'])
    def test_sai_port_attr_qos_tc_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_TC_TO_QUEUE_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_tc_and_color_to_dot1p_map_set')
    def test_sai_port_attr_qos_tc_and_color_to_dot1p_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DOT1P_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_tc_and_color_to_dot1p_map_set']
    )
    def test_sai_port_attr_qos_tc_and_color_to_dot1p_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DOT1P_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_tc_and_color_to_dscp_map_set')
    def test_sai_port_attr_qos_tc_and_color_to_dscp_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DSCP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_tc_and_color_to_dscp_map_set']
    )
    def test_sai_port_attr_qos_tc_and_color_to_dscp_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_DSCP_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_tc_to_priority_group_map_set')
    def test_sai_port_attr_qos_tc_to_priority_group_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_TC_TO_PRIORITY_GROUP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_tc_to_priority_group_map_set']
    )
    def test_sai_port_attr_qos_tc_to_priority_group_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_TC_TO_PRIORITY_GROUP_MAP'],
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

    @pytest.mark.dependency(
        name='test_sai_port_attr_qos_pfc_priority_to_priority_group_map_set'
    )
    def test_sai_port_attr_qos_pfc_priority_to_priority_group_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_PRIORITY_GROUP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_pfc_priority_to_priority_group_map_set']
    )
    def test_sai_port_attr_qos_pfc_priority_to_priority_group_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_PRIORITY_GROUP_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_pfc_priority_to_queue_map_set')
    def test_sai_port_attr_qos_pfc_priority_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_pfc_priority_to_queue_map_set']
    )
    def test_sai_port_attr_qos_pfc_priority_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_PFC_PRIORITY_TO_QUEUE_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_scheduler_profile_id_set')
    def test_sai_port_attr_qos_scheduler_profile_id_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_SCHEDULER_PROFILE_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_scheduler_profile_id_set'])
    def test_sai_port_attr_qos_scheduler_profile_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_SCHEDULER_PROFILE_ID'],
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

    @pytest.mark.dependency(
        name='test_sai_port_attr_qos_ingress_buffer_profile_list_set'
    )
    def test_sai_port_attr_qos_ingress_buffer_profile_list_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_INGRESS_BUFFER_PROFILE_LIST',
                    'empty',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_ingress_buffer_profile_list_set']
    )
    def test_sai_port_attr_qos_ingress_buffer_profile_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_INGRESS_BUFFER_PROFILE_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_port_attr_qos_egress_buffer_profile_list_set'
    )
    def test_sai_port_attr_qos_egress_buffer_profile_list_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_QOS_EGRESS_BUFFER_PROFILE_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_egress_buffer_profile_list_set']
    )
    def test_sai_port_attr_qos_egress_buffer_profile_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_EGRESS_BUFFER_PROFILE_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_priority_flow_control_mode_set')
    def test_sai_port_attr_priority_flow_control_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_MODE',
                    'SAI_PORT_PRIORITY_FLOW_CONTROL_MODE_COMBINED',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_priority_flow_control_mode_set']
    )
    def test_sai_port_attr_priority_flow_control_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_PRIORITY_FLOW_CONTROL_MODE_COMBINED', (
            'Get error, expected SAI_PORT_PRIORITY_FLOW_CONTROL_MODE_COMBINED but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_priority_flow_control_set')
    def test_sai_port_attr_priority_flow_control_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_priority_flow_control_set'])
    def test_sai_port_attr_priority_flow_control_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_priority_flow_control_rx_set')
    def test_sai_port_attr_priority_flow_control_rx_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_RX', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_priority_flow_control_rx_set'])
    def test_sai_port_attr_priority_flow_control_rx_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_RX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_priority_flow_control_tx_set')
    def test_sai_port_attr_priority_flow_control_tx_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_TX', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_priority_flow_control_tx_set'])
    def test_sai_port_attr_priority_flow_control_tx_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_TX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_meta_data_set')
    def test_sai_port_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_META_DATA', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_meta_data_set'])
    def test_sai_port_attr_meta_data_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_META_DATA']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_egress_block_port_list_set')
    def test_sai_port_attr_egress_block_port_list_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EGRESS_BLOCK_PORT_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_egress_block_port_list_set'])
    def test_sai_port_attr_egress_block_port_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_EGRESS_BLOCK_PORT_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_hw_profile_id_set')
    def test_sai_port_attr_hw_profile_id_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_HW_PROFILE_ID', 'vendor'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_hw_profile_id_set'])
    def test_sai_port_attr_hw_profile_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_HW_PROFILE_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'vendor', 'Get error, expected vendor but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_eee_enable_set')
    def test_sai_port_attr_eee_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EEE_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_eee_enable_set'])
    def test_sai_port_attr_eee_enable_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_EEE_ENABLE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_eee_idle_time_set')
    def test_sai_port_attr_eee_idle_time_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EEE_IDLE_TIME', '2500'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_eee_idle_time_set'])
    def test_sai_port_attr_eee_idle_time_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_EEE_IDLE_TIME'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '2500', 'Get error, expected 2500 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_eee_wake_time_set')
    def test_sai_port_attr_eee_wake_time_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_EEE_WAKE_TIME', '5'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_eee_wake_time_set'])
    def test_sai_port_attr_eee_wake_time_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_EEE_WAKE_TIME'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '5', 'Get error, expected 5 but got %s' % r_value

    def test_sai_port_attr_port_pool_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PORT_POOL_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_isolation_group_set')
    def test_sai_port_attr_isolation_group_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ISOLATION_GROUP', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_isolation_group_set'])
    def test_sai_port_attr_isolation_group_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ISOLATION_GROUP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_pkt_tx_enable_set')
    def test_sai_port_attr_pkt_tx_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PKT_TX_ENABLE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_pkt_tx_enable_set'])
    def test_sai_port_attr_pkt_tx_enable_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PKT_TX_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'true', 'Get error, expected true but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_tam_object_set')
    def test_sai_port_attr_tam_object_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_TAM_OBJECT', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_tam_object_set'])
    def test_sai_port_attr_tam_object_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_TAM_OBJECT']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_serdes_preemphasis_set')
    def test_sai_port_attr_serdes_preemphasis_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_SERDES_PREEMPHASIS', 'internal'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_serdes_preemphasis_set'])
    def test_sai_port_attr_serdes_preemphasis_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SERDES_PREEMPHASIS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'internal', (
            'Get error, expected internal but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_serdes_idriver_set')
    def test_sai_port_attr_serdes_idriver_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_SERDES_IDRIVER', 'internal'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_serdes_idriver_set'])
    def test_sai_port_attr_serdes_idriver_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SERDES_IDRIVER'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'internal', (
            'Get error, expected internal but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_serdes_ipredriver_set')
    def test_sai_port_attr_serdes_ipredriver_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_SERDES_IPREDRIVER', 'internal'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_serdes_ipredriver_set'])
    def test_sai_port_attr_serdes_ipredriver_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SERDES_IPREDRIVER'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'internal', (
            'Get error, expected internal but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_link_training_enable_set')
    def test_sai_port_attr_link_training_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_LINK_TRAINING_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_link_training_enable_set'])
    def test_sai_port_attr_link_training_enable_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_LINK_TRAINING_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ptp_mode_set')
    def test_sai_port_attr_ptp_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PTP_MODE', 'SAI_PORT_PTP_MODE_NONE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ptp_mode_set'])
    def test_sai_port_attr_ptp_mode_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_PTP_MODE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_PTP_MODE_NONE', (
            'Get error, expected SAI_PORT_PTP_MODE_NONE but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_interface_type_set')
    def test_sai_port_attr_interface_type_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_INTERFACE_TYPE',
                    'SAI_PORT_INTERFACE_TYPE_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_interface_type_set'])
    def test_sai_port_attr_interface_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_INTERFACE_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_INTERFACE_TYPE_NONE', (
            'Get error, expected SAI_PORT_INTERFACE_TYPE_NONE but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_advertised_interface_type_set')
    def test_sai_port_attr_advertised_interface_type_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_INTERFACE_TYPE', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_advertised_interface_type_set']
    )
    def test_sai_port_attr_advertised_interface_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ADVERTISED_INTERFACE_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_prbs_polynomial_set')
    def test_sai_port_attr_prbs_polynomial_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PRBS_POLYNOMIAL', 'internal'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_prbs_polynomial_set'])
    def test_sai_port_attr_prbs_polynomial_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRBS_POLYNOMIAL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'internal', (
            'Get error, expected internal but got %s' % r_value
        )

    def test_sai_port_attr_port_serdes_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PORT_SERDES_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'internal', (
            'Get error, expected internal but got %s' % r_value
        )

    def test_sai_port_attr_link_training_failure_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_LINK_TRAINING_FAILURE_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_link_training_rx_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_LINK_TRAINING_RX_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_prbs_config_set')
    def test_sai_port_attr_prbs_config_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_PRBS_CONFIG',
                    'SAI_PORT_PRBS_CONFIG_DISABLE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_prbs_config_set'])
    def test_sai_port_attr_prbs_config_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_PRBS_CONFIG']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_PRBS_CONFIG_DISABLE', (
            'Get error, expected SAI_PORT_PRBS_CONFIG_DISABLE but got %s' % r_value
        )

    def test_sai_port_attr_prbs_lock_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRBS_LOCK_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_prbs_lock_loss_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRBS_LOCK_LOSS_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_prbs_rx_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRBS_RX_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_prbs_rx_state_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRBS_RX_STATE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_auto_neg_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_AUTO_NEG_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_disable_decrement_ttl_set')
    def test_sai_port_attr_disable_decrement_ttl_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_DISABLE_DECREMENT_TTL', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_disable_decrement_ttl_set'])
    def test_sai_port_attr_disable_decrement_ttl_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_DISABLE_DECREMENT_TTL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_qos_mpls_exp_to_tc_map_set')
    def test_sai_port_attr_qos_mpls_exp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_qos_mpls_exp_to_tc_map_set'])
    def test_sai_port_attr_qos_mpls_exp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_MPLS_EXP_TO_TC_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_qos_mpls_exp_to_color_map_set')
    def test_sai_port_attr_qos_mpls_exp_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_mpls_exp_to_color_map_set']
    )
    def test_sai_port_attr_qos_mpls_exp_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_MPLS_EXP_TO_COLOR_MAP'],
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

    @pytest.mark.dependency(
        name='test_sai_port_attr_qos_tc_and_color_to_mpls_exp_map_set'
    )
    def test_sai_port_attr_qos_tc_and_color_to_mpls_exp_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_tc_and_color_to_mpls_exp_map_set']
    )
    def test_sai_port_attr_qos_tc_and_color_to_mpls_exp_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_TC_AND_COLOR_TO_MPLS_EXP_MAP'],
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

    @pytest.mark.dependency(name='test_sai_port_attr_tpid_set')
    def test_sai_port_attr_tpid_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_TPID', '0x8100'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_tpid_set'])
    def test_sai_port_attr_tpid_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_TPID']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0x8100', 'Get error, expected 0x8100 but got %s' % r_value

    def test_sai_port_attr_err_status_list_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ERR_STATUS_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_fabric_attached_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FABRIC_ATTACHED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_fabric_attached_switch_type_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FABRIC_ATTACHED_SWITCH_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_fabric_attached_switch_id_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FABRIC_ATTACHED_SWITCH_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_fabric_attached_port_index_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FABRIC_ATTACHED_PORT_INDEX'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_fabric_reachability_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FABRIC_REACHABILITY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_system_port_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_SYSTEM_PORT']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_auto_neg_fec_mode_override_set')
    def test_sai_port_attr_auto_neg_fec_mode_override_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_AUTO_NEG_FEC_MODE_OVERRIDE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_auto_neg_fec_mode_override_set']
    )
    def test_sai_port_attr_auto_neg_fec_mode_override_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_AUTO_NEG_FEC_MODE_OVERRIDE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_loopback_mode_set')
    def test_sai_port_attr_loopback_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_LOOPBACK_MODE',
                    'SAI_PORT_LOOPBACK_MODE_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_loopback_mode_set'])
    def test_sai_port_attr_loopback_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_LOOPBACK_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_LOOPBACK_MODE_NONE', (
            'Get error, expected SAI_PORT_LOOPBACK_MODE_NONE but got %s' % r_value
        )

    def test_sai_port_attr_mdix_mode_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_MDIX_MODE_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_mdix_mode_config_set')
    def test_sai_port_attr_mdix_mode_config_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_MDIX_MODE_CONFIG',
                    'SAI_PORT_MDIX_MODE_CONFIG_AUTO',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_mdix_mode_config_set'])
    def test_sai_port_attr_mdix_mode_config_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_MDIX_MODE_CONFIG'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_MDIX_MODE_CONFIG_AUTO', (
            'Get error, expected SAI_PORT_MDIX_MODE_CONFIG_AUTO but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_auto_neg_config_mode_set')
    def test_sai_port_attr_auto_neg_config_mode_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_AUTO_NEG_CONFIG_MODE',
                    'SAI_PORT_AUTO_NEG_CONFIG_MODE_DISABLED',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_auto_neg_config_mode_set'])
    def test_sai_port_attr_auto_neg_config_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_AUTO_NEG_CONFIG_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_AUTO_NEG_CONFIG_MODE_DISABLED', (
            'Get error, expected SAI_PORT_AUTO_NEG_CONFIG_MODE_DISABLED but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_1000x_sgmii_slave_autodetect_set')
    def test_sai_port_attr_1000x_sgmii_slave_autodetect_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_1000X_SGMII_SLAVE_AUTODETECT', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_1000x_sgmii_slave_autodetect_set']
    )
    def test_sai_port_attr_1000x_sgmii_slave_autodetect_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_1000X_SGMII_SLAVE_AUTODETECT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_module_type_set')
    def test_sai_port_attr_module_type_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_MODULE_TYPE',
                    'SAI_PORT_MODULE_TYPE_1000BASE_X',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_module_type_set'])
    def test_sai_port_attr_module_type_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_MODULE_TYPE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_MODULE_TYPE_1000BASE_X', (
            'Get error, expected SAI_PORT_MODULE_TYPE_1000BASE_X but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_dual_media_set')
    def test_sai_port_attr_dual_media_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_DUAL_MEDIA', 'SAI_PORT_DUAL_MEDIA_NONE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_dual_media_set'])
    def test_sai_port_attr_dual_media_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_DUAL_MEDIA']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_DUAL_MEDIA_NONE', (
            'Get error, expected SAI_PORT_DUAL_MEDIA_NONE but got %s' % r_value
        )

    def test_sai_port_attr_auto_neg_fec_mode_extended_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_AUTO_NEG_FEC_MODE_EXTENDED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ipg_set')
    def test_sai_port_attr_ipg_set(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'set', 'attributes': ['SAI_PORT_ATTR_IPG', '96']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ipg_set'])
    def test_sai_port_attr_ipg_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_IPG']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '96', 'Get error, expected 96 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_global_flow_control_forward_set')
    def test_sai_port_attr_global_flow_control_forward_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_FORWARD', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_global_flow_control_forward_set']
    )
    def test_sai_port_attr_global_flow_control_forward_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_GLOBAL_FLOW_CONTROL_FORWARD'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_priority_flow_control_forward_set')
    def test_sai_port_attr_priority_flow_control_forward_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_FORWARD', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_priority_flow_control_forward_set']
    )
    def test_sai_port_attr_priority_flow_control_forward_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PRIORITY_FLOW_CONTROL_FORWARD'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_port_attr_qos_dscp_to_forwarding_class_map_set'
    )
    def test_sai_port_attr_qos_dscp_to_forwarding_class_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_DSCP_TO_FORWARDING_CLASS_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_dscp_to_forwarding_class_map_set']
    )
    def test_sai_port_attr_qos_dscp_to_forwarding_class_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_DSCP_TO_FORWARDING_CLASS_MAP'],
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

    @pytest.mark.dependency(
        name='test_sai_port_attr_qos_mpls_exp_to_forwarding_class_map_set'
    )
    def test_sai_port_attr_qos_mpls_exp_to_forwarding_class_map_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_QOS_MPLS_EXP_TO_FORWARDING_CLASS_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_qos_mpls_exp_to_forwarding_class_map_set']
    )
    def test_sai_port_attr_qos_mpls_exp_to_forwarding_class_map_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_QOS_MPLS_EXP_TO_FORWARDING_CLASS_MAP'],
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

    def test_sai_port_attr_ipsec_port_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_IPSEC_PORT']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_pfc_tc_dld_interval_range_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PFC_TC_DLD_INTERVAL_RANGE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_pfc_tc_dld_interval_set')
    def test_sai_port_attr_pfc_tc_dld_interval_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PFC_TC_DLD_INTERVAL', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_pfc_tc_dld_interval_set'])
    def test_sai_port_attr_pfc_tc_dld_interval_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PFC_TC_DLD_INTERVAL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    def test_sai_port_attr_pfc_tc_dlr_interval_range_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PFC_TC_DLR_INTERVAL_RANGE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_pfc_tc_dlr_interval_set')
    def test_sai_port_attr_pfc_tc_dlr_interval_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_PFC_TC_DLR_INTERVAL', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_pfc_tc_dlr_interval_set'])
    def test_sai_port_attr_pfc_tc_dlr_interval_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PFC_TC_DLR_INTERVAL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    def test_sai_port_attr_supported_link_training_mode_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_SUPPORTED_LINK_TRAINING_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_rx_signal_detect_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_RX_SIGNAL_DETECT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_rx_lock_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_RX_LOCK_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_pcs_rx_link_status_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_PCS_RX_LINK_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_port_attr_fec_alignment_lock_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FEC_ALIGNMENT_LOCK'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_fabric_isolate_set')
    def test_sai_port_attr_fabric_isolate_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_FABRIC_ISOLATE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_fabric_isolate_set'])
    def test_sai_port_attr_fabric_isolate_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_FABRIC_ISOLATE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    def test_sai_port_attr_max_fec_symbol_errors_detectable_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_MAX_FEC_SYMBOL_ERRORS_DETECTABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ars_enable_set')
    def test_sai_port_attr_ars_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ARS_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ars_enable_set'])
    def test_sai_port_attr_ars_enable_get(self, npu):
        commands = [
            {'name': 'port_1', 'op': 'get', 'attributes': ['SAI_PORT_ATTR_ARS_ENABLE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ars_port_load_scaling_factor_set')
    def test_sai_port_attr_ars_port_load_scaling_factor_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ARS_PORT_LOAD_SCALING_FACTOR', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_ars_port_load_scaling_factor_set']
    )
    def test_sai_port_attr_ars_port_load_scaling_factor_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ARS_PORT_LOAD_SCALING_FACTOR'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ars_port_load_past_enable_set')
    def test_sai_port_attr_ars_port_load_past_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ARS_PORT_LOAD_PAST_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_ars_port_load_past_enable_set']
    )
    def test_sai_port_attr_ars_port_load_past_enable_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ARS_PORT_LOAD_PAST_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ars_port_load_future_enable_set')
    def test_sai_port_attr_ars_port_load_future_enable_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ARS_PORT_LOAD_FUTURE_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_port_attr_ars_port_load_future_enable_set']
    )
    def test_sai_port_attr_ars_port_load_future_enable_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ARS_PORT_LOAD_FUTURE_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ars_alternate_path_set')
    def test_sai_port_attr_ars_alternate_path_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ARS_ALTERNATE_PATH', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ars_alternate_path_set'])
    def test_sai_port_attr_ars_alternate_path_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ARS_ALTERNATE_PATH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    def test_sai_port_attr_json_formatted_debug_data_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_JSON_FORMATTED_DEBUG_DATA'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ecmp_hash_algorithm_set')
    def test_sai_port_attr_ecmp_hash_algorithm_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_ATTR_ECMP_HASH_ALGORITHM',
                    'SAI_HASH_ALGORITHM_CRC',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ecmp_hash_algorithm_set'])
    def test_sai_port_attr_ecmp_hash_algorithm_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ECMP_HASH_ALGORITHM'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_HASH_ALGORITHM_CRC', (
            'Get error, expected SAI_HASH_ALGORITHM_CRC but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_port_attr_ecmp_hash_seed_set')
    def test_sai_port_attr_ecmp_hash_seed_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ECMP_HASH_SEED', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ecmp_hash_seed_set'])
    def test_sai_port_attr_ecmp_hash_seed_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ECMP_HASH_SEED'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_port_attr_ecmp_hash_offset_set')
    def test_sai_port_attr_ecmp_hash_offset_set(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'set',
                'attributes': ['SAI_PORT_ATTR_ECMP_HASH_OFFSET', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_attr_ecmp_hash_offset_set'])
    def test_sai_port_attr_ecmp_hash_offset_get(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'get',
                'attributes': ['SAI_PORT_ATTR_ECMP_HASH_OFFSET'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_port_remove(self, npu):
        commands = [{'name': 'port_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
