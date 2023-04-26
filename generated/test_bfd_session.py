

from pprint import pprint

import pytest


class TestSaiBfdSession:

    @pytest.mark.dependency(scope='session')
    def test_bfd_session_create(self, npu):

        commands = [{'name': 'bfd_session_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_BFD_SESSION', 'attributes': ['SAI_BFD_SESSION_ATTR_TYPE', 'sai_bfd_session_type_t', 'SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER', 'sai_object_id_t', 'SAI_BFD_SESSION_ATTR_PORT', 'sai_object_id_t', 'SAI_BFD_SESSION_ATTR_LOCAL_DISCRIMINATOR', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_REMOTE_DISCRIMINATOR', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_UDP_SRC_PORT', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_VLAN_ID', '10', 'SAI_BFD_SESSION_ATTR_BFD_ENCAPSULATION_TYPE', 'sai_bfd_encapsulation_type_t', 'SAI_BFD_SESSION_ATTR_IPHDR_VERSION', 'sai_uint8_t', 'SAI_BFD_SESSION_ATTR_SRC_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_DST_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_TUNNEL_SRC_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_TUNNEL_DST_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS', 'sai_mac_t', 'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS', 'sai_mac_t', 'SAI_BFD_SESSION_ATTR_MIN_TX', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_MIN_RX', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_MULTIPLIER', 'sai_uint8_t', 'SAI_BFD_SESSION_ATTR_SRV6_SIDLIST_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_bfd_session_remove(self, npu):

        commands = [{'name': 'bfd_session_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_BFD_SESSION', 'attributes': ['SAI_BFD_SESSION_ATTR_TYPE', 'sai_bfd_session_type_t', 'SAI_BFD_SESSION_ATTR_VIRTUAL_ROUTER', 'sai_object_id_t', 'SAI_BFD_SESSION_ATTR_PORT', 'sai_object_id_t', 'SAI_BFD_SESSION_ATTR_LOCAL_DISCRIMINATOR', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_REMOTE_DISCRIMINATOR', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_UDP_SRC_PORT', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_VLAN_ID', '10', 'SAI_BFD_SESSION_ATTR_BFD_ENCAPSULATION_TYPE', 'sai_bfd_encapsulation_type_t', 'SAI_BFD_SESSION_ATTR_IPHDR_VERSION', 'sai_uint8_t', 'SAI_BFD_SESSION_ATTR_SRC_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_DST_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_TUNNEL_SRC_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_TUNNEL_DST_IP_ADDRESS', 'sai_ip_address_t', 'SAI_BFD_SESSION_ATTR_SRC_MAC_ADDRESS', 'sai_mac_t', 'SAI_BFD_SESSION_ATTR_DST_MAC_ADDRESS', 'sai_mac_t', 'SAI_BFD_SESSION_ATTR_MIN_TX', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_MIN_RX', 'sai_uint32_t', 'SAI_BFD_SESSION_ATTR_MULTIPLIER', 'sai_uint8_t', 'SAI_BFD_SESSION_ATTR_SRV6_SIDLIST_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
