from pprint import pprint

import pytest


class TestSaiNextHopGroup:
    # object with no parents

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

    def test_sai_next_hop_group_attr_next_hop_count_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_NEXT_HOP_COUNT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_next_hop_group_attr_next_hop_member_list_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_NEXT_HOP_MEMBER_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_next_hop_group_attr_set_switchover_set')
    def test_sai_next_hop_group_attr_set_switchover_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'set',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_SET_SWITCHOVER', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_next_hop_group_attr_set_switchover_set'])
    def test_sai_next_hop_group_attr_set_switchover_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_SET_SWITCHOVER'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_next_hop_group_attr_counter_id_set')
    def test_sai_next_hop_group_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'set',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_ATTR_COUNTER_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_next_hop_group_attr_counter_id_set'])
    def test_sai_next_hop_group_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_COUNTER_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    def test_sai_next_hop_group_attr_real_size_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_REAL_SIZE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_next_hop_group_attr_selection_map_set')
    def test_sai_next_hop_group_attr_selection_map_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'set',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_ATTR_SELECTION_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_next_hop_group_attr_selection_map_set'])
    def test_sai_next_hop_group_attr_selection_map_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_SELECTION_MAP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_next_hop_group_attr_ars_object_id_set')
    def test_sai_next_hop_group_attr_ars_object_id_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'set',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_ATTR_ARS_OBJECT_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_next_hop_group_attr_ars_object_id_set'])
    def test_sai_next_hop_group_attr_ars_object_id_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_ARS_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    def test_sai_next_hop_group_attr_ars_packet_drops_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_ARS_PACKET_DROPS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_next_hop_group_attr_ars_next_hop_reassignments_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_ARS_NEXT_HOP_REASSIGNMENTS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_next_hop_group_attr_ars_port_reassignments_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_ATTR_ARS_PORT_REASSIGNMENTS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_next_hop_group_remove(self, npu):
        commands = [{'name': 'next_hop_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
