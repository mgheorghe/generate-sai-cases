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

    @pytest.mark.dependency()
    def test_sai_tam_transport_attr_src_port_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': ['SAI_TAM_TRANSPORT_ATTR_SRC_PORT', '31337'],
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
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_SRC_PORT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '31337', (
            'Get error, expected 31337 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_transport_attr_dst_port_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': ['SAI_TAM_TRANSPORT_ATTR_DST_PORT', '31337'],
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
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_DST_PORT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '31337', (
            'Get error, expected 31337 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_transport_attr_transport_auth_type_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': [
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
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_AUTH_TYPE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_TAM_TRANSPORT_AUTH_TYPE_NONE', (
            'Get error, expected SAI_TAM_TRANSPORT_AUTH_TYPE_NONE but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_transport_attr_mtu_set(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': ['SAI_TAM_TRANSPORT_ATTR_MTU', '1500'],
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
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_MTU',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '1500', (
            'Get error, expected 1500 but got %s' % results[1][0].value()
        )

    def test_tam_transport_remove(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'attributes': [
                    'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_TYPE',
                    'SAI_TAM_TRANSPORT_TYPE_TCP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
