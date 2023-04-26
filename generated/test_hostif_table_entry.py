

from pprint import pprint

import pytest


class TestSaiHostifTableEntry:

    @pytest.mark.dependency(scope='session')
    def test_hostif_table_entry_create(self, npu):

        commands = [{'name': 'hostif_table_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY', 'attributes': ['SAI_HOSTIF_TABLE_ENTRY_ATTR_TYPE', 'sai_hostif_table_entry_type_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_OBJ_ID', 'sai_object_id_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_TRAP_ID', 'sai_object_id_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_CHANNEL_TYPE', 'sai_hostif_table_entry_channel_type_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_HOST_IF', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_hostif_table_entry_remove(self, npu):

        commands = [{'name': 'hostif_table_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY', 'attributes': ['SAI_HOSTIF_TABLE_ENTRY_ATTR_TYPE', 'sai_hostif_table_entry_type_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_OBJ_ID', 'sai_object_id_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_TRAP_ID', 'sai_object_id_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_CHANNEL_TYPE', 'sai_hostif_table_entry_channel_type_t', 'SAI_HOSTIF_TABLE_ENTRY_ATTR_HOST_IF', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

