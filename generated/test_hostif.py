from pprint import pprint

import pytest


class TestSaiHostif:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_VLAN SAI_OBJECT_TYPE_SYSTEM_PORT

    @pytest.mark.dependency(scope='session')
    def test_hostif_create(self, npu):
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
                'name': 'hostif_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF',
                'attributes': [
                    'SAI_HOSTIF_ATTR_TYPE',
                    'SAI_HOSTIF_TYPE_NETDEV',
                    'SAI_HOSTIF_ATTR_OBJ_ID',
                    '$port_1',
                    'SAI_HOSTIF_ATTR_NAME',
                    'char',
                    'SAI_HOSTIF_ATTR_GENETLINK_MCGRP_NAME',
                    'char',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_hostif_remove(self, npu):
        commands = [
            {
                'name': 'hostif_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF',
                'attributes': [
                    'SAI_HOSTIF_ATTR_TYPE',
                    'SAI_HOSTIF_TYPE_NETDEV',
                    'SAI_HOSTIF_ATTR_OBJ_ID',
                    '$port_1',
                    'SAI_HOSTIF_ATTR_NAME',
                    'char',
                    'SAI_HOSTIF_ATTR_GENETLINK_MCGRP_NAME',
                    'char',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
