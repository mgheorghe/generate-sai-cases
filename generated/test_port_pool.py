from pprint import pprint

import pytest


class TestSaiPortPool:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_BUFFER_POOL

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

    @pytest.mark.dependency(name='test_sai_port_pool_attr_qos_wred_profile_id_set')
    def test_sai_port_pool_attr_qos_wred_profile_id_set(self, npu):
        commands = [
            {
                'name': 'port_pool_1',
                'op': 'set',
                'attributes': [
                    'SAI_PORT_POOL_ATTR_QOS_WRED_PROFILE_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_port_pool_attr_qos_wred_profile_id_set'])
    def test_sai_port_pool_attr_qos_wred_profile_id_get(self, npu):
        commands = [
            {
                'name': 'port_pool_1',
                'op': 'get',
                'attributes': ['SAI_PORT_POOL_ATTR_QOS_WRED_PROFILE_ID'],
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

    def test_port_pool_remove(self, npu):
        commands = [
            {'name': 'port_pool_1', 'op': 'remove'},
            {'name': 'buffer_pool_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
