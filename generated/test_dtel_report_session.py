from pprint import pprint

import pytest


class TestSaiDtelReportSession:
    # object with no attributes

    def test_dtel_report_session_create(self, npu):
        commands = [
            {
                'name': 'dtel_report_session_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_dtel_report_session_attr_src_ip_set(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_src_ip_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': ['SAI_DTEL_REPORT_SESSION_ATTR_SRC_IP', '0.0.0.0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_src_ip_get(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_src_ip_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': 'SAI_DTEL_REPORT_SESSION_ATTR_SRC_IP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0.0.0.0' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_dst_ip_list_set(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_dst_ip_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': ['SAI_DTEL_REPORT_SESSION_ATTR_DST_IP_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_dst_ip_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_dst_ip_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': 'SAI_DTEL_REPORT_SESSION_ATTR_DST_IP_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_virtual_router_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_virtual_router_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': [
                    'SAI_DTEL_REPORT_SESSION_ATTR_VIRTUAL_ROUTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_virtual_router_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_virtual_router_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': 'SAI_DTEL_REPORT_SESSION_ATTR_VIRTUAL_ROUTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_truncate_size_set(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_truncate_size_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': ['SAI_DTEL_REPORT_SESSION_ATTR_TRUNCATE_SIZE', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_truncate_size_get(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_truncate_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': 'SAI_DTEL_REPORT_SESSION_ATTR_TRUNCATE_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_udp_dst_port_set(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_udp_dst_port_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': ['SAI_DTEL_REPORT_SESSION_ATTR_UDP_DST_PORT', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_dtel_report_session_attr_udp_dst_port_get(self, dpu):
        commands = [
            {
                'name': 'sai_dtel_report_session_attr_udp_dst_port_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'atrribute': 'SAI_DTEL_REPORT_SESSION_ATTR_UDP_DST_PORT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_dtel_report_session_remove(self, npu):
        commands = [
            {
                'name': 'dtel_report_session_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
