from pprint import pprint

import pytest


class TestSaiPortConnector:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_PORT

    @pytest.mark.dependency(scope='session')
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

    def test_sai_port_connector_attr_failover_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_port_connector_attr_failover_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR',
                'atrribute': [
                    'SAI_PORT_CONNECTOR_ATTR_FAILOVER_MODE',
                    'SAI_PORT_CONNECTOR_FAILOVER_MODE_DISABLE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_port_connector_attr_failover_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_port_connector_attr_failover_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR',
                'atrribute': 'SAI_PORT_CONNECTOR_ATTR_FAILOVER_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PORT_CONNECTOR_FAILOVER_MODE_DISABLE' for result in results]
        ), 'Get error'

    def test_port_connector_remove(self, npu):
        commands = [
            {
                'name': 'port_connector_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR',
                'attributes': [
                    'SAI_PORT_CONNECTOR_ATTR_SYSTEM_SIDE_PORT_ID',
                    '$port_1',
                    'SAI_PORT_CONNECTOR_ATTR_LINE_SIDE_PORT_ID',
                    '$port_1',
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
