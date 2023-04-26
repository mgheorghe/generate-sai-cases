

from pprint import pprint

import pytest


class TestSaiMcastFdbEntry:

    @pytest.mark.dependency(scope='session')
    def test_mcast_fdb_entry_create(self, npu):

        commands = [{'name': 'mcast_fdb_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY', 'attributes': ['SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID', 'sai_object_id_t', 'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION', 'sai_packet_action_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_mcast_fdb_entry_remove(self, npu):

        commands = [{'name': 'mcast_fdb_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY', 'attributes': ['SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID', 'sai_object_id_t', 'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION', 'sai_packet_action_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

