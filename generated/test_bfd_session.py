from pprint import pprint

import pytest


class TestSaiBfdSession:
    # object with parent SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SRV6_SIDLIST

    @pytest.mark.dependency(scope='session')
    def test_bfd_session_create(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
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
                'name': 'srv6_sidlist_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            },
            {
                'name': 'bfd_session_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'attributes': [
                    'SAI_BFD_SESSION_ATTR_TYPE',
                    'SAI_BFD_SESSION_TYPE_DEMAND_ACTIVE',
                    'SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER',
                    '$virtual_router_1',
                    'SAI_BFD_SESSION_ATTR_PORT',
                    '$port_1',
                    'SAI_BFD_SESSION_ATTR_LOCAL_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_REMOTE_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_BFD_SESSION_ATTR_VLAN_ID',
                    '10',
                    'SAI_BFD_SESSION_ATTR_BFD_ENCAPSULATION_TYPE',
                    'SAI_BFD_ENCAPSULATION_TYPE_IP_IN_IP',
                    'SAI_BFD_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_MIN_TX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MIN_RX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MULTIPLIER',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_bfd_session_remove(self, npu):
        commands = [
            {
                'name': 'bfd_session_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BFD_SESSION',
                'attributes': [
                    'SAI_BFD_SESSION_ATTR_TYPE',
                    'SAI_BFD_SESSION_TYPE_DEMAND_ACTIVE',
                    'SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER',
                    '$virtual_router_1',
                    'SAI_BFD_SESSION_ATTR_PORT',
                    '$port_1',
                    'SAI_BFD_SESSION_ATTR_LOCAL_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_REMOTE_DISCRIMINATOR',
                    '10',
                    'SAI_BFD_SESSION_ATTR_UDP_SRC_PORT',
                    '10',
                    'SAI_BFD_SESSION_ATTR_VLAN_ID',
                    '10',
                    'SAI_BFD_SESSION_ATTR_BFD_ENCAPSULATION_TYPE',
                    'SAI_BFD_ENCAPSULATION_TYPE_IP_IN_IP',
                    'SAI_BFD_SESSION_ATTR_IPHDR_VERSION',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_SRC_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_TUNNEL_DST_IP_ADDRESS',
                    'sai_ip_address_t',
                    'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                    'SAI_BFD_SESSION_ATTR_MIN_TX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MIN_RX',
                    '10',
                    'SAI_BFD_SESSION_ATTR_MULTIPLIER',
                    'sai_uint8_t',
                    'SAI_BFD_SESSION_ATTR_SRV6_SIDLIST_ID',
                    '$srv6_sidlist_1',
                ],
            },
            {
                'name': 'srv6_sidlist_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
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
            {
                'name': 'virtual_router_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
