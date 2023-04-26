

from pprint import pprint

import pytest


class TestSaiMacsecFlow:

    @pytest.mark.dependency(scope='session')
    def test_macsec_flow_create(self, npu):

        commands = [{'name': 'macsec_flow_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW', 'attributes': ['SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_macsec_flow_remove(self, npu):

        commands = [{'name': 'macsec_flow_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW', 'attributes': ['SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION', 'sai_macsec_direction_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

