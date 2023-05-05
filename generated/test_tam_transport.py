from pprint import pprint

import pytest


class TestSaiTamTransport:
    # object with no parents

    def test_tam_transport_create(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'attributes': [
                    'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_TYPE',
                    'SAI_TAM_TRANSPORT_TYPE_TCP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_tam_transport_attr_src_port_set')
    def test_sai_tam_transport_attr_src_port_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'set',
                'attributes': ['SAI_TAM_TRANSPORT_ATTR_SRC_PORT', '31337'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_transport_attr_src_port_set'])
    def test_sai_tam_transport_attr_src_port_get(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'attributes': ['SAI_TAM_TRANSPORT_ATTR_SRC_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '31337', 'Get error, expected 31337 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_transport_attr_dst_port_set')
    def test_sai_tam_transport_attr_dst_port_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'set',
                'attributes': ['SAI_TAM_TRANSPORT_ATTR_DST_PORT', '31337'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_transport_attr_dst_port_set'])
    def test_sai_tam_transport_attr_dst_port_get(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'attributes': ['SAI_TAM_TRANSPORT_ATTR_DST_PORT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '31337', 'Get error, expected 31337 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_tam_transport_attr_transport_auth_type_set')
    def test_sai_tam_transport_attr_transport_auth_type_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'set',
                'attributes': [
                    'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_AUTH_TYPE',
                    'SAI_TAM_TRANSPORT_AUTH_TYPE_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_transport_attr_transport_auth_type_set']
    )
    def test_sai_tam_transport_attr_transport_auth_type_get(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'attributes': ['SAI_TAM_TRANSPORT_ATTR_TRANSPORT_AUTH_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_TAM_TRANSPORT_AUTH_TYPE_NONE', (
            'Get error, expected SAI_TAM_TRANSPORT_AUTH_TYPE_NONE but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_tam_transport_attr_mtu_set')
    def test_sai_tam_transport_attr_mtu_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'set',
                'attributes': ['SAI_TAM_TRANSPORT_ATTR_MTU', '1500'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_transport_attr_mtu_set'])
    def test_sai_tam_transport_attr_mtu_get(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'attributes': ['SAI_TAM_TRANSPORT_ATTR_MTU'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '1500', 'Get error, expected 1500 but got %s' % r_value

    def test_tam_transport_remove(self, npu):
        commands = [{'name': 'tam_transport_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
