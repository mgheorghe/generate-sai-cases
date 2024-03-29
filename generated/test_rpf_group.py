from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiRpfGroup:
    # object with no attributes

    def test_rpf_group_create(self, npu):
        commands = [
            {
                'name': 'rpf_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_RPF_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_sai_rpf_group_attr_rpf_interface_count_get(self, npu):
        commands = [
            {
                'name': 'rpf_group_1',
                'op': 'get',
                'attributes': ['SAI_RPF_GROUP_ATTR_RPF_INTERFACE_COUNT'],
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

    def test_sai_rpf_group_attr_rpf_member_list_get(self, npu):
        commands = [
            {
                'name': 'rpf_group_1',
                'op': 'get',
                'attributes': ['SAI_RPF_GROUP_ATTR_RPF_MEMBER_LIST'],
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

    def test_rpf_group_remove(self, npu):
        commands = [{'name': 'rpf_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
