from pprint import pprint

import pytest


class TestSaiNextHopGroup:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_next_hop_group_create(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_ATTR_TYPE',
                    'SAI_NEXT_HOP_GROUP_TYPE_DYNAMIC_UNORDERED_ECMP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_next_hop_group_attr_next_hop_count_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_next_hop_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_NEXT_HOP_COUNT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_next_hop_member_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_next_hop_member_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_NEXT_HOP_MEMBER_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_set_switchover_set(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_set_switchover_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': ['SAI_NEXT_HOP_GROUP_ATTR_SET_SWITCHOVER', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_set_switchover_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_set_switchover_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_SET_SWITCHOVER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': [
                    'SAI_NEXT_HOP_GROUP_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_real_size_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_real_size_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_REAL_SIZE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_selection_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_selection_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': [
                    'SAI_NEXT_HOP_GROUP_ATTR_SELECTION_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_selection_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_selection_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_SELECTION_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_ars_object_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_ars_object_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': [
                    'SAI_NEXT_HOP_GROUP_ATTR_ARS_OBJECT_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_ars_object_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_ars_object_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_ARS_OBJECT_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_ars_packet_drops_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_ars_packet_drops_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_ARS_PACKET_DROPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_ars_next_hop_reassignments_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_ars_next_hop_reassignments_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_ARS_NEXT_HOP_REASSIGNMENTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_next_hop_group_attr_ars_port_reassignments_get(self, dpu):
        commands = [
            {
                'name': 'sai_next_hop_group_attr_ars_port_reassignments_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'atrribute': 'SAI_NEXT_HOP_GROUP_ATTR_ARS_PORT_REASSIGNMENTS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_next_hop_group_remove(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_ATTR_TYPE',
                    'SAI_NEXT_HOP_GROUP_TYPE_DYNAMIC_UNORDERED_ECMP',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
