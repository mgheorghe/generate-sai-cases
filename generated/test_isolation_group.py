from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiIsolationGroup:
    # object with no parents

    def test_isolation_group_create(self, npu):
        commands = [
            {
                'name': 'isolation_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ISOLATION_GROUP',
                'attributes': [
                    'SAI_ISOLATION_GROUP_ATTR_TYPE',
                    'SAI_ISOLATION_GROUP_TYPE_PORT',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_sai_isolation_group_attr_isolation_member_list_get(self, npu):
        commands = [
            {
                'name': 'isolation_group_1',
                'op': 'get',
                'attributes': ['SAI_ISOLATION_GROUP_ATTR_ISOLATION_MEMBER_LIST'],
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

    def test_isolation_group_remove(self, npu):
        commands = [{'name': 'isolation_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
