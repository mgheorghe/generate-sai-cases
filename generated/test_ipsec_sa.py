

from pprint import pprint

import pytest


class TestSaiIpsecSa:

    @pytest.mark.dependency(scope='session')
    def test_ipsec_sa_create(self, npu):

        commands = [{'name': 'ipsec_sa_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_IPSEC_SA', 'attributes': ['SAI_IPSEC_SA_ATTR_IPSEC_DIRECTION', 'sai_ipsec_direction_t', 'SAI_IPSEC_SA_ATTR_IPSEC_ID', 'sai_object_id_t', 'SAI_IPSEC_SA_ATTR_IPSEC_SPI', 'sai_uint32_t', 'SAI_IPSEC_SA_ATTR_ENCRYPT_KEY', 'sai_encrypt_key_t', 'SAI_IPSEC_SA_ATTR_SALT', 'sai_uint32_t', 'SAI_IPSEC_SA_ATTR_AUTH_KEY', 'sai_auth_key_t', 'SAI_IPSEC_SA_ATTR_TERM_DST_IP', 'sai_ip_address_t', 'SAI_IPSEC_SA_ATTR_TERM_VLAN_ID', '10', 'SAI_IPSEC_SA_ATTR_TERM_SRC_IP', 'sai_ip_address_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_ipsec_sa_remove(self, npu):

        commands = [{'name': 'ipsec_sa_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_IPSEC_SA', 'attributes': ['SAI_IPSEC_SA_ATTR_IPSEC_DIRECTION', 'sai_ipsec_direction_t', 'SAI_IPSEC_SA_ATTR_IPSEC_ID', 'sai_object_id_t', 'SAI_IPSEC_SA_ATTR_IPSEC_SPI', 'sai_uint32_t', 'SAI_IPSEC_SA_ATTR_ENCRYPT_KEY', 'sai_encrypt_key_t', 'SAI_IPSEC_SA_ATTR_SALT', 'sai_uint32_t', 'SAI_IPSEC_SA_ATTR_AUTH_KEY', 'sai_auth_key_t', 'SAI_IPSEC_SA_ATTR_TERM_DST_IP', 'sai_ip_address_t', 'SAI_IPSEC_SA_ATTR_TERM_VLAN_ID', '10', 'SAI_IPSEC_SA_ATTR_TERM_SRC_IP', 'sai_ip_address_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

