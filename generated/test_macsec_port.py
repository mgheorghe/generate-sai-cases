

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_PORT
class TestSaiMacsecPort:

    @pytest.mark.dependency(scope='session')
    def test_macsec_port_create(self, npu):

        commands = [{'name': 'macsec_port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC_PORT', 'attributes': ['SAI_MACSEC_PORT_ATTR_MACSEC_DIRECTION', 'SAI_MACSEC_DIRECTION_EGRESS', 'SAI_MACSEC_PORT_ATTR_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_macsec_port_remove(self, npu):

        commands = [{'name': 'macsec_port_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MACSEC_PORT', 'attributes': ['SAI_MACSEC_PORT_ATTR_MACSEC_DIRECTION', 'SAI_MACSEC_DIRECTION_EGRESS', 'SAI_MACSEC_PORT_ATTR_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

