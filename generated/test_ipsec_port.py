from pprint import pprint

import pytest


class TestSaiIpsecPort:
    # object with parent SAI_OBJECT_TYPE_PORT

    @pytest.mark.dependency(scope='session')
    def test_ipsec_port_create(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'ipsec_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'attributes': [
                    'SAI_IPSEC_PORT_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_IPSEC_PORT_ATTR_NATIVE_VLAN_ID',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_ipsec_port_attr_ctag_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_ctag_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': ['SAI_IPSEC_PORT_ATTR_CTAG_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_port_attr_ctag_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_ctag_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': 'SAI_IPSEC_PORT_ATTR_CTAG_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_ipsec_port_attr_stag_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_stag_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': ['SAI_IPSEC_PORT_ATTR_STAG_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_port_attr_stag_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_stag_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': 'SAI_IPSEC_PORT_ATTR_STAG_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_ipsec_port_attr_vrf_from_packet_vlan_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_vrf_from_packet_vlan_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': [
                    'SAI_IPSEC_PORT_ATTR_VRF_FROM_PACKET_VLAN_ENABLE',
                    'false',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_port_attr_vrf_from_packet_vlan_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_vrf_from_packet_vlan_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': 'SAI_IPSEC_PORT_ATTR_VRF_FROM_PACKET_VLAN_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_ipsec_port_attr_switch_switching_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_switch_switching_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': [
                    'SAI_IPSEC_PORT_ATTR_SWITCH_SWITCHING_MODE',
                    'SAI_SWITCH_SWITCHING_MODE_CUT_THROUGH',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ipsec_port_attr_switch_switching_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_ipsec_port_attr_switch_switching_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'atrribute': 'SAI_IPSEC_PORT_ATTR_SWITCH_SWITCHING_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_SWITCH_SWITCHING_MODE_CUT_THROUGH' for result in results]
        ), 'Get error'

    def test_ipsec_port_remove(self, npu):
        commands = [
            {
                'name': 'ipsec_port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'attributes': [
                    'SAI_IPSEC_PORT_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_IPSEC_PORT_ATTR_NATIVE_VLAN_ID',
                    '10',
                ],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
