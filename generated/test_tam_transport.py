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

    def test_sai_tam_transport_attr_src_port_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_src_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': ['SAI_TAM_TRANSPORT_ATTR_SRC_PORT', '31337'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_transport_attr_src_port_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_src_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_SRC_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '31337' for result in results]), 'Get error'

    def test_sai_tam_transport_attr_dst_port_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_dst_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': ['SAI_TAM_TRANSPORT_ATTR_DST_PORT', '31337'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_transport_attr_dst_port_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_dst_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_DST_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '31337' for result in results]), 'Get error'

    def test_sai_tam_transport_attr_transport_auth_type_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_transport_auth_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': [
                    'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_AUTH_TYPE',
                    'SAI_TAM_TRANSPORT_AUTH_TYPE_NONE',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_transport_attr_transport_auth_type_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_transport_auth_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_AUTH_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_TAM_TRANSPORT_AUTH_TYPE_NONE' for result in results]
        ), 'Get error'

    def test_sai_tam_transport_attr_mtu_set(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_mtu_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': ['SAI_TAM_TRANSPORT_ATTR_MTU', '1500'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_transport_attr_mtu_get(self, npu):
        commands = [
            {
                'name': 'sai_tam_transport_attr_mtu_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'atrribute': 'SAI_TAM_TRANSPORT_ATTR_MTU',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1500' for result in results]), 'Get error'

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
