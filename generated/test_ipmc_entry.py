

from pprint import pprint

import pytest


class TestSaiIpmcEntry:

    @pytest.mark.dependency(scope='session')
    def test_ipmc_entry_create(self, npu):

        commands = [{'name': 'ipmc_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY', 'attributes': ['SAI_IPMC_ENTRY_ATTR_PACKET_ACTION', 'sai_packet_action_t', 'SAI_IPMC_ENTRY_ATTR_RPF_GROUP_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_ipmc_entry_remove(self, npu):

        commands = [{'name': 'ipmc_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY', 'attributes': ['SAI_IPMC_ENTRY_ATTR_PACKET_ACTION', 'sai_packet_action_t', 'SAI_IPMC_ENTRY_ATTR_RPF_GROUP_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
