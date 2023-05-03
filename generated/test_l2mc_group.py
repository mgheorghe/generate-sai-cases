from pprint import pprint


class TestSaiL2McGroup:
    # object with no attributes

    def test_l2mc_group_create(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_l2mc_group_attr_l2mc_output_count_get(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'atrribute': 'SAI_L2MC_GROUP_ATTR_L2MC_OUTPUT_COUNT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_sai_l2mc_group_attr_l2mc_member_list_get(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'atrribute': 'SAI_L2MC_GROUP_ATTR_L2MC_MEMBER_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_l2mc_group_remove(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
