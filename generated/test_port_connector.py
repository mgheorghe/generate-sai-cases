from pprint import pprint

import pytest


class TestSaiPortConnector:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_PORT

    def test_port_connector_create(self, npu):
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
                'name': 'port_connector_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR',
                'attributes': [
                    'SAI_PORT_CONNECTOR_ATTR_SYSTEM_SIDE_PORT_ID',
                    '$port_1',
                    'SAI_PORT_CONNECTOR_ATTR_LINE_SIDE_PORT_ID',
                    '$port_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_port_connector_attr_failover_mode_set')
    def test_sai_port_connector_attr_failover_mode_set(self, npu):
        commands = [
            {
                'name': 'port_connector_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_CONNECTOR_ATTR_FAILOVER_MODE',
                    'SAI_PORT_CONNECTOR_FAILOVER_MODE_DISABLE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_connector_attr_failover_mode_set'])
    def test_sai_port_connector_attr_failover_mode_get(self, npu):
        commands = [
            {
                'name': 'port_connector_1',
                'op': 'get',
                'attributes': ['SAI_PORT_CONNECTOR_ATTR_FAILOVER_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PORT_CONNECTOR_FAILOVER_MODE_DISABLE', (
            'Get error, expected SAI_PORT_CONNECTOR_FAILOVER_MODE_DISABLE but got %s'
            % r_value
        )

    def test_port_connector_remove(self, npu):
        commands = [
            {'name': 'port_connector_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
