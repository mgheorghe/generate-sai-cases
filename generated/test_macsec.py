

from pprint import pprint

import pytest

# object with no parents
class TestSaiMacsec:

    @pytest.mark.dependency(scope='session')
    def test_macsec_create(self, npu):

        commands = [{'name': 'macsec_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC', 'attributes': ['SAI_MACSEC_ATTR_DIRECTION', 'sai_macsec_direction_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_macsec_remove(self, npu):

        commands = [{'name': 'macsec_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MACSEC', 'attributes': ['SAI_MACSEC_ATTR_DIRECTION', 'sai_macsec_direction_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

