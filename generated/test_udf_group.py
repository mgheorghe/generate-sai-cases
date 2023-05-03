from pprint import pprint


class TestSaiUdfGroup:
    # object with no parents

    def test_udf_group_create(self, npu):
        commands = [
            {
                'name': 'udf_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'attributes': ['SAI_UDF_GROUP_ATTR_LENGTH', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_udf_group_attr_udf_list_get(self, npu):
        commands = [
            {
                'name': 'udf_group_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'atrribute': 'SAI_UDF_GROUP_ATTR_UDF_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_udf_group_remove(self, npu):
        commands = [
            {
                'name': 'udf_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'attributes': ['SAI_UDF_GROUP_ATTR_LENGTH', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
