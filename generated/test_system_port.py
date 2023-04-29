from pprint import pprint

import pytest


class TestSaiSystemPort:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_system_port_create(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'attributes': [
                    'SAI_SYSTEM_PORT_ATTR_CONFIG_INFO',
                    'sai_system_port_config_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_system_port_attr_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_system_port_attr_qos_number_of_voqs_get(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_qos_number_of_voqs_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_QOS_NUMBER_OF_VOQS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_system_port_attr_qos_voq_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_qos_voq_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_QOS_VOQ_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_system_port_attr_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_system_port_attr_admin_state_set(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_admin_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': ['SAI_SYSTEM_PORT_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_system_port_attr_admin_state_get(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_admin_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_ADMIN_STATE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_system_port_attr_qos_tc_to_queue_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_qos_tc_to_queue_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': [
                    'SAI_SYSTEM_PORT_ATTR_QOS_TC_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_system_port_attr_qos_tc_to_queue_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_system_port_attr_qos_tc_to_queue_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_QOS_TC_TO_QUEUE_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_system_port_remove(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'attributes': [
                    'SAI_SYSTEM_PORT_ATTR_CONFIG_INFO',
                    'sai_system_port_config_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
