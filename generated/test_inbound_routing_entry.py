

from pprint import pprint

import pytest

# object with no attributes
class TestSaiInboundRoutingEntry:

    @pytest.mark.dependency(scope='session')
    def test_inbound_routing_entry_create(self, npu):

        commands = [{'name': 'inbound_routing_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_inbound_routing_entry_remove(self, npu):

        commands = [{'name': 'inbound_routing_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

