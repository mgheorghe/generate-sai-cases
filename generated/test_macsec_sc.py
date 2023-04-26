

from pprint import pprint

import pytest


class TestSaiMacsecSc:

    @pytest.mark.dependency(scope='session')
    def test_macsec_sc_create(self, npu):

        commands = [{'name': 'macsec_sc_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC_SC', 'attributes': ['SAI_MACSEC_SC_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t', 'SAI_MACSEC_SC_ATTR_FLOW_ID', 'sai_object_id_t', 'SAI_MACSEC_SC_ATTR_MACSEC_SCI', 'sai_uint64_t', 'SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE', 'sai_macsec_cipher_suite_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_macsec_sc_remove(self, npu):

        commands = [{'name': 'macsec_sc_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MACSEC_SC', 'attributes': ['SAI_MACSEC_SC_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t', 'SAI_MACSEC_SC_ATTR_FLOW_ID', 'sai_object_id_t', 'SAI_MACSEC_SC_ATTR_MACSEC_SCI', 'sai_uint64_t', 'SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE', 'sai_macsec_cipher_suite_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

