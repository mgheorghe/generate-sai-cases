

from pprint import pprint

import pytest


class TestSaiMacsecSa:

    @pytest.mark.dependency(scope='session')
    def test_macsec_sa_create(self, npu):

        commands = [{'name': 'macsec_sa_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC_SA', 'attributes': ['SAI_MACSEC_SA_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t', 'SAI_MACSEC_SA_ATTR_SC_ID', 'sai_object_id_t', 'SAI_MACSEC_SA_ATTR_AN', 'sai_uint8_t', 'SAI_MACSEC_SA_ATTR_SAK', 'sai_macsec_sak_t', 'SAI_MACSEC_SA_ATTR_SALT', 'sai_macsec_salt_t', 'SAI_MACSEC_SA_ATTR_AUTH_KEY', 'sai_macsec_auth_key_t', 'SAI_MACSEC_SA_ATTR_MACSEC_SSCI', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_macsec_sa_remove(self, npu):

        commands = [{'name': 'macsec_sa_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MACSEC_SA', 'attributes': ['SAI_MACSEC_SA_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t', 'SAI_MACSEC_SA_ATTR_SC_ID', 'sai_object_id_t', 'SAI_MACSEC_SA_ATTR_AN', 'sai_uint8_t', 'SAI_MACSEC_SA_ATTR_SAK', 'sai_macsec_sak_t', 'SAI_MACSEC_SA_ATTR_SALT', 'sai_macsec_salt_t', 'SAI_MACSEC_SA_ATTR_AUTH_KEY', 'sai_macsec_auth_key_t', 'SAI_MACSEC_SA_ATTR_MACSEC_SSCI', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
