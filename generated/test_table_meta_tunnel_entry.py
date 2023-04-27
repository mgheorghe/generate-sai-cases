from pprint import pprint

import pytest


class TestSaiTableMetaTunnelEntry:
    # object with parent SAI_OBJECT_TYPE_TUNNEL

    @pytest.mark.dependency(scope='session')
    def test_table_meta_tunnel_entry_create(self, npu):
        commands = [
            {
                'name': 'table_meta_tunnel_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TABLE_META_TUNNEL_ENTRY',
                'attributes': [
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_ACTION',
                    'sai_table_meta_tunnel_entry_action_t',
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_METADATA_KEY',
                    '10',
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_TUNNEL_ID',
                    'sai_object_id_t',
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_UNDERLAY_DIP',
                    'sai_ip_address_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_table_meta_tunnel_entry_remove(self, npu):
        commands = [
            {
                'name': 'table_meta_tunnel_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TABLE_META_TUNNEL_ENTRY',
                'attributes': [
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_ACTION',
                    'sai_table_meta_tunnel_entry_action_t',
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_METADATA_KEY',
                    '10',
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_TUNNEL_ID',
                    'sai_object_id_t',
                    'SAI_TABLE_META_TUNNEL_ENTRY_ATTR_UNDERLAY_DIP',
                    'sai_ip_address_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
