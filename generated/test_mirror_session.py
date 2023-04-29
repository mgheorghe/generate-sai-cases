from pprint import pprint

import pytest


class TestSaiMirrorSession:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT

    @pytest.mark.dependency(scope='session')
    def test_mirror_session_create(self, npu):
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
                'name': 'mirror_session_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'attributes': [
                    'SAI_MIRROR_SESSION_ATTR_TYPE',
                    'SAI_MIRROR_SESSION_TYPE_LOCAL',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORT',
                    '$port_1',
                    'SAI_MIRROR_SESSION_ATTR_ERSPAN_ENCAPSULATION_TYPE',
                    'SAI_ERSPAN_ENCAPSULATION_TYPE_MIRROR_L3_GRE_TUNNEL',
                    'SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_TOS',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST',
                    'sai_object_list_t',
                    'SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_mirror_session_remove(self, npu):
        commands = [
            {
                'name': 'mirror_session_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION',
                'attributes': [
                    'SAI_MIRROR_SESSION_ATTR_TYPE',
                    'SAI_MIRROR_SESSION_TYPE_LOCAL',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORT',
                    '$port_1',
                    'SAI_MIRROR_SESSION_ATTR_ERSPAN_ENCAPSULATION_TYPE',
                    'SAI_ERSPAN_ENCAPSULATION_TYPE_MIRROR_L3_GRE_TUNNEL',
                    'SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_TOS',
                    'sai_uint8_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST',
                    'sai_object_list_t',
                    'SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
