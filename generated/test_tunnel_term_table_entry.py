from pprint import pprint

import pytest


class TestSaiTunnelTermTableEntry:
    # object with parent SAI_OBJECT_TYPE_VIRTUAL_ROUTER SAI_OBJECT_TYPE_TUNNEL

    @pytest.mark.dependency(scope='session')
    def test_tunnel_term_table_entry_create(self, npu):
        commands = [
            {
                'name': 'tunnel_term_table_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_TERM_TABLE_ENTRY',
                'attributes': [
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_VR_ID',
                    'sai_object_id_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_TYPE',
                    'sai_tunnel_term_table_entry_type_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_DST_IP',
                    'sai_ip_address_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_SRC_IP',
                    'sai_ip_address_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_TUNNEL_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_ACTION_TUNNEL_ID',
                    'sai_object_id_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_tunnel_term_table_entry_remove(self, npu):
        commands = [
            {
                'name': 'tunnel_term_table_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_TERM_TABLE_ENTRY',
                'attributes': [
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_VR_ID',
                    'sai_object_id_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_TYPE',
                    'sai_tunnel_term_table_entry_type_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_DST_IP',
                    'sai_ip_address_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_SRC_IP',
                    'sai_ip_address_t',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_TUNNEL_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_TERM_TABLE_ENTRY_ATTR_ACTION_TUNNEL_ID',
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
