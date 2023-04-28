from pprint import pprint

import pytest


class TestSaiUdf:
    # object with parent SAI_OBJECT_TYPE_UDF_MATCH SAI_OBJECT_TYPE_UDF_GROUP

    @pytest.mark.dependency(scope='session')
    def test_udf_create(self, npu):
        commands = [
            {
                'name': 'udf_match_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_UDF_MATCH',
                'attributes': [],
            },
            {
                'name': 'udf_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'attributes': ['SAI_UDF_GROUP_ATTR_LENGTH', '10'],
            },
            {
                'name': 'udf_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'attributes': [
                    'SAI_UDF_ATTR_MATCH_ID',
                    '$udf_match_1',
                    'SAI_UDF_ATTR_GROUP_ID',
                    '$udf_group_1',
                    'SAI_UDF_ATTR_OFFSET',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_udf_remove(self, npu):
        commands = [
            {
                'name': 'udf_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'attributes': [
                    'SAI_UDF_ATTR_MATCH_ID',
                    '$udf_match_1',
                    'SAI_UDF_ATTR_GROUP_ID',
                    '$udf_group_1',
                    'SAI_UDF_ATTR_OFFSET',
                    '10',
                ],
            },
            {
                'name': 'udf_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'attributes': ['SAI_UDF_GROUP_ATTR_LENGTH', '10'],
            },
            {
                'name': 'udf_match_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_UDF_MATCH',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
