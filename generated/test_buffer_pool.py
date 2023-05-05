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
                'name': 'buffer_pool_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_POOL_ATTR_SHARED_SIZE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_pool_attr_size_set')
    def test_sai_buffer_pool_attr_size_set(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_POOL_ATTR_SIZE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_buffer_pool_attr_size_set'])
    def test_sai_buffer_pool_attr_size_get(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_POOL_ATTR_SIZE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_pool_attr_tam_set')
    def test_sai_buffer_pool_attr_tam_set(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_POOL_ATTR_TAM', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_buffer_pool_attr_tam_set'])
    def test_sai_buffer_pool_attr_tam_get(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_POOL_ATTR_TAM'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_pool_attr_xoff_size_set')
    def test_sai_buffer_pool_attr_xoff_size_set(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_POOL_ATTR_XOFF_SIZE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_buffer_pool_attr_xoff_size_set'])
    def test_sai_buffer_pool_attr_xoff_size_get(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_POOL_ATTR_XOFF_SIZE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_pool_attr_wred_profile_id_set')
    def test_sai_buffer_pool_attr_wred_profile_id_set(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'set',
                'attributes': [
                    'SAI_BUFFER_POOL_ATTR_WRED_PROFILE_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_buffer_pool_attr_wred_profile_id_set'])
    def test_sai_buffer_pool_attr_wred_profile_id_get(self, npu):
        commands = [
            {
                'name': 'buffer_pool_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_POOL_ATTR_WRED_PROFILE_ID'],
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

    def test_buffer_pool_remove(self, npu):
        commands = [{'name': 'buffer_pool_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
