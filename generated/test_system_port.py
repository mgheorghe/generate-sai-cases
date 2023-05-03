from pprint import pprint

import pytest


class TestSaiSystemPort:
    # object with no parents

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

    def test_sai_system_port_attr_type_get(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_TYPE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_sai_system_port_attr_qos_number_of_voqs_get(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_QOS_NUMBER_OF_VOQS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_sai_system_port_attr_qos_voq_list_get(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_QOS_VOQ_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_sai_system_port_attr_port_get(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_PORT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_system_port_attr_admin_state_set(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': ['SAI_SYSTEM_PORT_ATTR_ADMIN_STATE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_system_port_attr_admin_state_set'])
    def test_sai_system_port_attr_admin_state_get(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_ADMIN_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_system_port_attr_qos_tc_to_queue_map_set(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': [
                    'SAI_SYSTEM_PORT_ATTR_QOS_TC_TO_QUEUE_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_system_port_attr_qos_tc_to_queue_map_set']
    )
    def test_sai_system_port_attr_qos_tc_to_queue_map_get(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'atrribute': 'SAI_SYSTEM_PORT_ATTR_QOS_TC_TO_QUEUE_MAP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

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
