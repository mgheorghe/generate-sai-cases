from pprint import pprint

import pytest


class TestSaiTamCollector:
    # object with parent SAI_OBJECT_TYPE_TAM_TRANSPORT

    @pytest.mark.dependency(scope='session')
    def test_tam_collector_create(self, npu):
        commands = [
            {
                'name': 'tam_transport_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'attributes': [
                    'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_TYPE',
                    'SAI_TAM_TRANSPORT_TYPE_TCP',
                ],
            },
            {
                'name': 'tam_collector_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'attributes': [
                    'SAI_TAM_COLLECTOR_ATTR_SRC_IP',
                    'sai_ip_address_t',
                    'SAI_TAM_COLLECTOR_ATTR_DST_IP',
                    'sai_ip_address_t',
                    'SAI_TAM_COLLECTOR_ATTR_TRANSPORT',
                    '$tam_transport_1',
                    'SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE',
                    'sai_uint8_t',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tam_collector_attr_src_ip_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_src_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': ['SAI_TAM_COLLECTOR_ATTR_SRC_IP', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_src_ip_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_src_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': 'SAI_TAM_COLLECTOR_ATTR_SRC_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_dst_ip_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_dst_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': ['SAI_TAM_COLLECTOR_ATTR_DST_IP', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_dst_ip_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_dst_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': 'SAI_TAM_COLLECTOR_ATTR_DST_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_localhost_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_localhost_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': ['SAI_TAM_COLLECTOR_ATTR_LOCALHOST', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_localhost_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_localhost_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': 'SAI_TAM_COLLECTOR_ATTR_LOCALHOST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_virtual_router_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_virtual_router_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': [
                    'SAI_TAM_COLLECTOR_ATTR_VIRTUAL_ROUTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_virtual_router_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_virtual_router_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': 'SAI_TAM_COLLECTOR_ATTR_VIRTUAL_ROUTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_truncate_size_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_truncate_size_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': ['SAI_TAM_COLLECTOR_ATTR_TRUNCATE_SIZE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_truncate_size_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_truncate_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': 'SAI_TAM_COLLECTOR_ATTR_TRUNCATE_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_transport_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_transport_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': ['SAI_TAM_COLLECTOR_ATTR_TRANSPORT', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_transport_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_transport_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': 'SAI_TAM_COLLECTOR_ATTR_TRANSPORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_dscp_value_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_dscp_value_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': ['SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_collector_attr_dscp_value_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_collector_attr_dscp_value_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'atrribute': 'SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_tam_collector_remove(self, npu):
        commands = [
            {
                'name': 'tam_collector_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR',
                'attributes': [
                    'SAI_TAM_COLLECTOR_ATTR_SRC_IP',
                    'sai_ip_address_t',
                    'SAI_TAM_COLLECTOR_ATTR_DST_IP',
                    'sai_ip_address_t',
                    'SAI_TAM_COLLECTOR_ATTR_TRANSPORT',
                    '$tam_transport_1',
                    'SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE',
                    'sai_uint8_t',
                ],
            },
            {
                'name': 'tam_transport_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT',
                'attributes': [
                    'SAI_TAM_TRANSPORT_ATTR_TRANSPORT_TYPE',
                    'SAI_TAM_TRANSPORT_TYPE_TCP',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
