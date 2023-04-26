

from pprint import pprint

import pytest


class TestSaiMirrorSession:

    @pytest.mark.dependency(scope='session')
    def test_mirror_session_create(self, npu):

        commands = [{'name': 'mirror_session_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION', 'attributes': ['SAI_MIRROR_SESSION_ATTR_TYPE', 'sai_mirror_session_type_t', 'SAI_MIRROR_SESSION_ATTR_MONITOR_PORT', 'sai_object_id_t', 'SAI_MIRROR_SESSION_ATTR_ERSPAN_ENCAPSULATION_TYPE', 'sai_erspan_encapsulation_type_t', 'SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION', 'sai_uint8_t', 'SAI_MIRROR_SESSION_ATTR_TOS', 'sai_uint8_t', 'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS', 'sai_ip_address_t', 'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS', 'sai_ip_address_t', 'SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS', 'sai_mac_t', 'SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS', 'sai_mac_t', 'SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE', '10', 'SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST', 'sai_object_list_t', 'SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT', '10', 'SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_mirror_session_remove(self, npu):

        commands = [{'name': 'mirror_session_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION', 'attributes': ['SAI_MIRROR_SESSION_ATTR_TYPE', 'sai_mirror_session_type_t', 'SAI_MIRROR_SESSION_ATTR_MONITOR_PORT', 'sai_object_id_t', 'SAI_MIRROR_SESSION_ATTR_ERSPAN_ENCAPSULATION_TYPE', 'sai_erspan_encapsulation_type_t', 'SAI_MIRROR_SESSION_ATTR_IPHDR_VERSION', 'sai_uint8_t', 'SAI_MIRROR_SESSION_ATTR_TOS', 'sai_uint8_t', 'SAI_MIRROR_SESSION_ATTR_SRC_IP_ADDRESS', 'sai_ip_address_t', 'SAI_MIRROR_SESSION_ATTR_DST_IP_ADDRESS', 'sai_ip_address_t', 'SAI_MIRROR_SESSION_ATTR_SRC_MAC_ADDRESS', 'sai_mac_t', 'SAI_MIRROR_SESSION_ATTR_DST_MAC_ADDRESS', 'sai_mac_t', 'SAI_MIRROR_SESSION_ATTR_GRE_PROTOCOL_TYPE', '10', 'SAI_MIRROR_SESSION_ATTR_MONITOR_PORTLIST', 'sai_object_list_t', 'SAI_MIRROR_SESSION_ATTR_UDP_SRC_PORT', '10', 'SAI_MIRROR_SESSION_ATTR_UDP_DST_PORT', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
