from pprint import pprint

import pytest


class TestSaiPortPool:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_BUFFER_POOL

    @pytest.mark.dependency(scope='session')
    def test_port_pool_create(self, npu):
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
                'name': 'buffer_pool_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'attributes': [
                    'SAI_BUFFER_POOL_ATTR_TYPE',
                    'SAI_BUFFER_POOL_TYPE_INGRESS',
                    'SAI_BUFFER_POOL_ATTR_SIZE',
                    '10',
                ],
            },
            {
                'name': 'port_pool_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT_POOL',
                'attributes': [
                    'SAI_PORT_POOL_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_PORT_POOL_ATTR_BUFFER_POOL_ID',
                    '$buffer_pool_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_port_pool_remove(self, npu):
        commands = [
            {
                'name': 'port_pool_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT_POOL',
                'attributes': [
                    'SAI_PORT_POOL_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_PORT_POOL_ATTR_BUFFER_POOL_ID',
                    '$buffer_pool_1',
                ],
            },
            {
                'name': 'buffer_pool_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'attributes': [
                    'SAI_BUFFER_POOL_ATTR_TYPE',
                    'SAI_BUFFER_POOL_TYPE_INGRESS',
                    'SAI_BUFFER_POOL_ATTR_SIZE',
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
