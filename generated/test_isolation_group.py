from pprint import pprint


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
        assert all(results), 'Create error'

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
        pprint(results)
        assert results[0][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_isolation_group_remove(self, npu):
        commands = [{'name': 'isolation_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
