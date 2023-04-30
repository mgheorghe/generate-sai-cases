from pprint import pprint

import pytest


class TestSaiStp:
    # object with no attributes

    def test_stp_create(self, npu):
        commands = [
            {
                'name': 'stp_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_STP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_stp_attr_vlan_list_get(self, npu):
        commands = [
            {
                'name': 'sai_stp_attr_vlan_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_STP',
                'atrribute': 'SAI_STP_ATTR_VLAN_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_stp_attr_bridge_id_get(self, npu):
        commands = [
            {
                'name': 'sai_stp_attr_bridge_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_STP',
                'atrribute': 'SAI_STP_ATTR_BRIDGE_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_stp_attr_port_list_get(self, npu):
        commands = [
            {
                'name': 'sai_stp_attr_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_STP',
                'atrribute': 'SAI_STP_ATTR_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_stp_remove(self, npu):
        commands = [
            {
                'name': 'stp_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_STP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
