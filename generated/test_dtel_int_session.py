from pprint import pprint

import pytest


class TestSaiDtelIntSession:
    # object with no attributes

    def test_dtel_int_session_create(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_dtel_int_session_attr_max_hop_count_set(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': ['SAI_DTEL_INT_SESSION_ATTR_MAX_HOP_COUNT', '8'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_dtel_int_session_attr_max_hop_count_set']
    )
    def test_sai_dtel_int_session_attr_max_hop_count_get(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': 'SAI_DTEL_INT_SESSION_ATTR_MAX_HOP_COUNT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '8', (
            'Get error, expected 8 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_int_session_attr_collect_switch_id_set(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': ['SAI_DTEL_INT_SESSION_ATTR_COLLECT_SWITCH_ID', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_dtel_int_session_attr_collect_switch_id_set']
    )
    def test_sai_dtel_int_session_attr_collect_switch_id_get(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': 'SAI_DTEL_INT_SESSION_ATTR_COLLECT_SWITCH_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_int_session_attr_collect_switch_ports_set(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': [
                    'SAI_DTEL_INT_SESSION_ATTR_COLLECT_SWITCH_PORTS',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_dtel_int_session_attr_collect_switch_ports_set']
    )
    def test_sai_dtel_int_session_attr_collect_switch_ports_get(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': 'SAI_DTEL_INT_SESSION_ATTR_COLLECT_SWITCH_PORTS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_int_session_attr_collect_ingress_timestamp_set(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': [
                    'SAI_DTEL_INT_SESSION_ATTR_COLLECT_INGRESS_TIMESTAMP',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_dtel_int_session_attr_collect_ingress_timestamp_set']
    )
    def test_sai_dtel_int_session_attr_collect_ingress_timestamp_get(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': 'SAI_DTEL_INT_SESSION_ATTR_COLLECT_INGRESS_TIMESTAMP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_int_session_attr_collect_egress_timestamp_set(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': [
                    'SAI_DTEL_INT_SESSION_ATTR_COLLECT_EGRESS_TIMESTAMP',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_dtel_int_session_attr_collect_egress_timestamp_set']
    )
    def test_sai_dtel_int_session_attr_collect_egress_timestamp_get(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': 'SAI_DTEL_INT_SESSION_ATTR_COLLECT_EGRESS_TIMESTAMP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_int_session_attr_collect_queue_info_set(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': ['SAI_DTEL_INT_SESSION_ATTR_COLLECT_QUEUE_INFO', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_dtel_int_session_attr_collect_queue_info_set']
    )
    def test_sai_dtel_int_session_attr_collect_queue_info_get(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'atrribute': 'SAI_DTEL_INT_SESSION_ATTR_COLLECT_QUEUE_INFO',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    def test_dtel_int_session_remove(self, npu):
        commands = [
            {
                'name': 'dtel_int_session_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DTEL_INT_SESSION',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
