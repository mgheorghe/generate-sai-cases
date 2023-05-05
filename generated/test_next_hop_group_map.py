from pprint import pprint

import pytest


class TestSaiNextHopGroupMap:
    # object with no parents

    def test_next_hop_group_map_create(self, npu):
        commands = [
            {
                'name': 'next_hop_group_map_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NEXT_HOP_GROUP_MAP',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_MAP_ATTR_TYPE',
                    'SAI_NEXT_HOP_GROUP_MAP_TYPE_FORWARDING_CLASS_TO_INDEX',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(
        name='test_sai_next_hop_group_map_attr_map_to_value_list_set'
    )
    def test_sai_next_hop_group_map_attr_map_to_value_list_set(self, npu):
        commands = [
            {
                'name': 'next_hop_group_map_1',
                'op': 'set',
                'attributes': [
                    'SAI_NEXT_HOP_GROUP_MAP_ATTR_MAP_TO_VALUE_LIST',
                    'empty',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_next_hop_group_map_attr_map_to_value_list_set']
    )
    def test_sai_next_hop_group_map_attr_map_to_value_list_get(self, npu):
        commands = [
            {
                'name': 'next_hop_group_map_1',
                'op': 'get',
                'attributes': ['SAI_NEXT_HOP_GROUP_MAP_ATTR_MAP_TO_VALUE_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' % r_value

    def test_next_hop_group_map_remove(self, npu):
        commands = [{'name': 'next_hop_group_map_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
