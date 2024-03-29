from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiBufferProfile:
    # object with parent SAI_OBJECT_TYPE_BUFFER_POOL

    def test_buffer_profile_create(self, npu):
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
            },
            {
                'name': 'buffer_profile_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BUFFER_PROFILE',
                'attributes': [
                    'SAI_BUFFER_PROFILE_ATTR_POOL_ID',
                    '$buffer_pool_1',
                    'SAI_BUFFER_PROFILE_ATTR_RESERVED_BUFFER_SIZE',
                    '10',
                    'SAI_BUFFER_PROFILE_ATTR_THRESHOLD_MODE',
                    'SAI_BUFFER_PROFILE_THRESHOLD_MODE_STATIC',
                    'SAI_BUFFER_PROFILE_ATTR_SHARED_DYNAMIC_TH',
                    '1',
                    'SAI_BUFFER_PROFILE_ATTR_SHARED_STATIC_TH',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(
        name='test_sai_buffer_profile_attr_reserved_buffer_size_set'
    )
    def test_sai_buffer_profile_attr_reserved_buffer_size_set(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_RESERVED_BUFFER_SIZE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_buffer_profile_attr_reserved_buffer_size_set']
    )
    def test_sai_buffer_profile_attr_reserved_buffer_size_get(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_RESERVED_BUFFER_SIZE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_profile_attr_shared_dynamic_th_set')
    def test_sai_buffer_profile_attr_shared_dynamic_th_set(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_SHARED_DYNAMIC_TH', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_buffer_profile_attr_shared_dynamic_th_set']
    )
    def test_sai_buffer_profile_attr_shared_dynamic_th_get(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_SHARED_DYNAMIC_TH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_profile_attr_shared_static_th_set')
    def test_sai_buffer_profile_attr_shared_static_th_set(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_SHARED_STATIC_TH', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_buffer_profile_attr_shared_static_th_set']
    )
    def test_sai_buffer_profile_attr_shared_static_th_get(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_SHARED_STATIC_TH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_profile_attr_xoff_th_set')
    def test_sai_buffer_profile_attr_xoff_th_set(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_XOFF_TH', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_buffer_profile_attr_xoff_th_set'])
    def test_sai_buffer_profile_attr_xoff_th_get(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_XOFF_TH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_profile_attr_xon_th_set')
    def test_sai_buffer_profile_attr_xon_th_set(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_XON_TH', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_buffer_profile_attr_xon_th_set'])
    def test_sai_buffer_profile_attr_xon_th_get(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_XON_TH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_buffer_profile_attr_xon_offset_th_set')
    def test_sai_buffer_profile_attr_xon_offset_th_set(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'set',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_XON_OFFSET_TH', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_buffer_profile_attr_xon_offset_th_set'])
    def test_sai_buffer_profile_attr_xon_offset_th_get(self, npu):
        commands = [
            {
                'name': 'buffer_profile_1',
                'op': 'get',
                'attributes': ['SAI_BUFFER_PROFILE_ATTR_XON_OFFSET_TH'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_buffer_profile_remove(self, npu):
        commands = [
            {'name': 'buffer_profile_1', 'op': 'remove'},
            {'name': 'buffer_pool_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
