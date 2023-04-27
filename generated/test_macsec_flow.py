

from pprint import pprint

import pytest

# object with no parents
class TestSaiMacsecFlow:

    @pytest.mark.dependency(scope='session')
    def test_macsec_flow_create(self, npu):

        commands = [{'name': 'macsec_flow_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW', 'attributes': ['SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION', 'SAI_MACSEC_DIRECTION_EGRESS']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_macsec_flow_remove(self, npu):

        commands = [{'name': 'macsec_flow_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW', 'attributes': ['SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION', 'SAI_MACSEC_DIRECTION_EGRESS']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

