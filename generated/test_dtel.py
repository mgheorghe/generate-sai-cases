from pprint import pprint

import pytest


class TestSaiDtel:
    # object with no attributes

    def test_dtel_create(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_dtel_attr_int_endpoint_enable_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_INT_ENDPOINT_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_int_endpoint_enable_set'])
    def test_sai_dtel_attr_int_endpoint_enable_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_INT_ENDPOINT_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_int_transit_enable_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_INT_TRANSIT_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_int_transit_enable_set'])
    def test_sai_dtel_attr_int_transit_enable_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_INT_TRANSIT_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_postcard_enable_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_POSTCARD_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_postcard_enable_set'])
    def test_sai_dtel_attr_postcard_enable_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_POSTCARD_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_drop_report_enable_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_DROP_REPORT_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_drop_report_enable_set'])
    def test_sai_dtel_attr_drop_report_enable_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_DROP_REPORT_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_queue_report_enable_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_QUEUE_REPORT_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_queue_report_enable_set'])
    def test_sai_dtel_attr_queue_report_enable_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_QUEUE_REPORT_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_switch_id_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_SWITCH_ID', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_switch_id_set'])
    def test_sai_dtel_attr_switch_id_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_SWITCH_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_flow_state_clear_cycle_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_FLOW_STATE_CLEAR_CYCLE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_flow_state_clear_cycle_set'])
    def test_sai_dtel_attr_flow_state_clear_cycle_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_FLOW_STATE_CLEAR_CYCLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_latency_sensitivity_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_LATENCY_SENSITIVITY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_latency_sensitivity_set'])
    def test_sai_dtel_attr_latency_sensitivity_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_LATENCY_SENSITIVITY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_sink_port_list_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_SINK_PORT_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_sink_port_list_set'])
    def test_sai_dtel_attr_sink_port_list_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_SINK_PORT_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'empty', (
            'Get error, expected empty but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_dtel_attr_int_l4_dscp_set(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': ['SAI_DTEL_ATTR_INT_L4_DSCP', 'disabled'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_dtel_attr_int_l4_dscp_set'])
    def test_sai_dtel_attr_int_l4_dscp_get(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'atrribute': 'SAI_DTEL_ATTR_INT_L4_DSCP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'disabled', (
            'Get error, expected disabled but got %s' % results[1][0].value()
        )

    def test_dtel_remove(self, npu):
        commands = [
            {
                'name': 'dtel_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_DTEL',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
