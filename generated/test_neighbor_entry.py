from pprint import pprint

import pytest


class TestSaiNeighborEntry:
    # object with no parents

    def test_neighbor_entry_create(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'attributes': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'rif_id': 'TODO',
                    'ip_address': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_dst_mac_address_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_neighbor_entry_attr_dst_mac_address_set']
    )
    def test_sai_neighbor_entry_attr_dst_mac_address_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_neighbor_entry_attr_packet_action_set'])
    def test_sai_neighbor_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_PACKET_ACTION_FORWARD', (
            'Get error, expected SAI_PACKET_ACTION_FORWARD but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_user_trap_id_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_USER_TRAP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_neighbor_entry_attr_user_trap_id_set'])
    def test_sai_neighbor_entry_attr_user_trap_id_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_USER_TRAP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_no_host_route_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_NO_HOST_ROUTE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_neighbor_entry_attr_no_host_route_set'])
    def test_sai_neighbor_entry_attr_no_host_route_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_NO_HOST_ROUTE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_META_DATA', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_neighbor_entry_attr_meta_data_set'])
    def test_sai_neighbor_entry_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_META_DATA',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_neighbor_entry_attr_counter_id_set'])
    def test_sai_neighbor_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_encap_index_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_INDEX', 'internal'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_neighbor_entry_attr_encap_index_set'])
    def test_sai_neighbor_entry_attr_encap_index_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_INDEX',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'internal', (
            'Get error, expected internal but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_encap_impose_index_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_IMPOSE_INDEX', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_neighbor_entry_attr_encap_impose_index_set']
    )
    def test_sai_neighbor_entry_attr_encap_impose_index_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_ENCAP_IMPOSE_INDEX',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_neighbor_entry_attr_is_local_set(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': ['SAI_NEIGHBOR_ENTRY_ATTR_IS_LOCAL', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_neighbor_entry_attr_is_local_set'])
    def test_sai_neighbor_entry_attr_is_local_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_IS_LOCAL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'true', (
            'Get error, expected true but got %s' % results[1][0].value()
        )

    def test_sai_neighbor_entry_attr_ip_addr_family_get(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'atrribute': 'SAI_NEIGHBOR_ENTRY_ATTR_IP_ADDR_FAMILY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_neighbor_entry_remove(self, npu):
        commands = [
            {
                'name': 'neighbor_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NEIGHBOR_ENTRY',
                'attributes': [
                    'SAI_NEIGHBOR_ENTRY_ATTR_DST_MAC_ADDRESS',
                    '00:00:B1:AE:C5:00',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'rif_id': 'TODO',
                    'ip_address': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
