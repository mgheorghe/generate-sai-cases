from pprint import pprint

import pytest


class TestSaiUdf:
    # object with parent SAI_OBJECT_TYPE_UDF_MATCH SAI_OBJECT_TYPE_UDF_GROUP

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

    @pytest.mark.dependency()
    def test_sai_udf_attr_base_set(self, npu):
        commands = [
            {
                'name': 'udf_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': ['SAI_UDF_ATTR_BASE', 'SAI_UDF_BASE_L2'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_udf_attr_base_set'])
    def test_sai_udf_attr_base_get(self, npu):
        commands = [
            {
                'name': 'udf_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': 'SAI_UDF_ATTR_BASE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_UDF_BASE_L2', (
            'Get error, expected SAI_UDF_BASE_L2 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_udf_attr_hash_mask_set(self, npu):
        commands = [
            {
                'name': 'udf_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': ['SAI_UDF_ATTR_HASH_MASK', 'const'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_udf_attr_hash_mask_set'])
    def test_sai_udf_attr_hash_mask_get(self, npu):
        commands = [
            {
                'name': 'udf_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': 'SAI_UDF_ATTR_HASH_MASK',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'const', (
            'Get error, expected const but got %s' % results[1][0].value()
        )

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
