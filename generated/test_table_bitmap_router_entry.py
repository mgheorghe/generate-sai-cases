

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_NEXT_HOP SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_HOSTIF_TRAP
class TestSaiTableBitmapRouterEntry:

    @pytest.mark.dependency(scope='session')
    def test_table_bitmap_router_entry_create(self, npu):

        commands = [{'name': 'table_bitmap_router_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TABLE_BITMAP_ROUTER_ENTRY', 'attributes': ['SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ACTION', 'sai_table_bitmap_router_entry_action_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_PRIORITY', 'sai_uint32_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_KEY', 'sai_uint32_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_MASK', 'sai_uint32_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_DST_IP_KEY', 'sai_ip_prefix_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TUNNEL_INDEX', '10', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_NEXT_HOP', 'sai_object_id_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ROUTER_INTERFACE', 'sai_object_id_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TRAP_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_table_bitmap_router_entry_remove(self, npu):

        commands = [{'name': 'table_bitmap_router_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TABLE_BITMAP_ROUTER_ENTRY', 'attributes': ['SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ACTION', 'sai_table_bitmap_router_entry_action_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_PRIORITY', 'sai_uint32_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_KEY', 'sai_uint32_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_IN_RIF_METADATA_MASK', 'sai_uint32_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_DST_IP_KEY', 'sai_ip_prefix_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TUNNEL_INDEX', '10', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_NEXT_HOP', 'sai_object_id_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_ROUTER_INTERFACE', 'sai_object_id_t', 'SAI_TABLE_BITMAP_ROUTER_ENTRY_ATTR_TRAP_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

