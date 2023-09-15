from pprint import pprint

import pytest


@pytest.mark.npu
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

    def test_sai_l2mc_group_attr_l2mc_output_count_get(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'get',
                'attributes': ['SAI_L2MC_GROUP_ATTR_L2MC_OUTPUT_COUNT'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_l2mc_group_attr_l2mc_member_list_get(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'get',
                'attributes': ['SAI_L2MC_GROUP_ATTR_L2MC_MEMBER_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_l2mc_group_remove(self, npu):
        commands = [{'name': 'l2mc_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
