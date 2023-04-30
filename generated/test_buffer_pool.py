from pprint import pprint

import pytest


class TestSaiBufferPool:
    # object with no parents

    def test_buffer_pool_create(self, npu):
        commands = [
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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_buffer_pool_attr_shared_size_get(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_shared_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': 'SAI_BUFFER_POOL_ATTR_SHARED_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_size_set(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_size_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': ['SAI_BUFFER_POOL_ATTR_SIZE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_size_get(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': 'SAI_BUFFER_POOL_ATTR_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_tam_set(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_tam_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': ['SAI_BUFFER_POOL_ATTR_TAM', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_tam_get(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_tam_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': 'SAI_BUFFER_POOL_ATTR_TAM',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_xoff_size_set(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_xoff_size_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': ['SAI_BUFFER_POOL_ATTR_XOFF_SIZE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_xoff_size_get(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_xoff_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': 'SAI_BUFFER_POOL_ATTR_XOFF_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_wred_profile_id_set(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_wred_profile_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': [
                    'SAI_BUFFER_POOL_ATTR_WRED_PROFILE_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_buffer_pool_attr_wred_profile_id_get(self, npu):
        commands = [
            {
                'name': 'sai_buffer_pool_attr_wred_profile_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BUFFER_POOL',
                'atrribute': 'SAI_BUFFER_POOL_ATTR_WRED_PROFILE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_buffer_pool_remove(self, npu):
        commands = [
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
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
