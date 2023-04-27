from pprint import pprint

import pytest


class TestSaiHostifTableEntry:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_HOSTIF_TRAP SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP SAI_OBJECT_TYPE_HOSTIF

    @pytest.mark.dependency(scope='session')
    def test_hostif_table_entry_create(self, npu):
        commands = [
            {
                'name': 'hostif_table_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY',
                'attributes': [
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TYPE',
                    'sai_hostif_table_entry_type_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_OBJ_ID',
                    'sai_object_id_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TRAP_ID',
                    'sai_object_id_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_CHANNEL_TYPE',
                    'sai_hostif_table_entry_channel_type_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_HOST_IF',
                    'sai_object_id_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_hostif_table_entry_remove(self, npu):
        commands = [
            {
                'name': 'hostif_table_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY',
                'attributes': [
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TYPE',
                    'sai_hostif_table_entry_type_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_OBJ_ID',
                    'sai_object_id_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TRAP_ID',
                    'sai_object_id_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_CHANNEL_TYPE',
                    'sai_hostif_table_entry_channel_type_t',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_HOST_IF',
                    'sai_object_id_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
