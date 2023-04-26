

from pprint import pprint

import pytest


class TestSaiMacsecPort:

    @pytest.mark.dependency(scope='session')
    def test_macsec_port_create(self, npu):

        commands = [{'name': 'macsec_port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC_PORT', 'attributes': ['SAI_MACSEC_PORT_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t', 'SAI_MACSEC_PORT_ATTR_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_macsec_port_remove(self, npu):

        commands = [{'name': 'macsec_port_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MACSEC_PORT', 'attributes': ['SAI_MACSEC_PORT_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t', 'SAI_MACSEC_PORT_ATTR_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

