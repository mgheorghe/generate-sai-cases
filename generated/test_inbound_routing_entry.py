

from pprint import pprint

import pytest


class TestSaiInboundRoutingEntry:

    @pytest.mark.dependency(scope='session')
    def test_inbound_routing_entry_create(self, npu):

        commands = [{'name': 'inbound_routing_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_inbound_routing_entry_remove(self, npu):

        commands = [{'name': 'inbound_routing_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
