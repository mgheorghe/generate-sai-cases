

from pprint import pprint

import pytest

# object with no attributes
class TestSaiOutboundCaToPaEntry:

    @pytest.mark.dependency(scope='session')
    def test_outbound_ca_to_pa_entry_create(self, npu):

        commands = [{'name': 'outbound_ca_to_pa_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_outbound_ca_to_pa_entry_remove(self, npu):

        commands = [{'name': 'outbound_ca_to_pa_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

