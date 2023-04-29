from pprint import pprint

import pytest


class TestSaiUdfGroup:
    # object with no parents

    @pytest.mark.dependency(scope='session')
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

    def test_sai_udf_group_attr_udf_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_udf_group_attr_udf_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'atrribute': 'SAI_UDF_GROUP_ATTR_UDF_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

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
