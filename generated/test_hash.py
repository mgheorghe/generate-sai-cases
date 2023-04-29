from pprint import pprint

import pytest


class TestSaiHash:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_hash_create(self, npu):
        commands = [
            {
                'name': 'hash_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_hash_attr_native_hash_field_list_set(self, dpu):
        commands = [
            {
                'name': 'sai_hash_attr_native_hash_field_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'atrribute': ['SAI_HASH_ATTR_NATIVE_HASH_FIELD_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hash_attr_native_hash_field_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_hash_attr_native_hash_field_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'atrribute': 'SAI_HASH_ATTR_NATIVE_HASH_FIELD_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_hash_attr_udf_group_list_set(self, dpu):
        commands = [
            {
                'name': 'sai_hash_attr_udf_group_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'atrribute': ['SAI_HASH_ATTR_UDF_GROUP_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hash_attr_udf_group_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_hash_attr_udf_group_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'atrribute': 'SAI_HASH_ATTR_UDF_GROUP_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_hash_attr_fine_grained_hash_field_list_set(self, dpu):
        commands = [
            {
                'name': 'sai_hash_attr_fine_grained_hash_field_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'atrribute': ['SAI_HASH_ATTR_FINE_GRAINED_HASH_FIELD_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_hash_attr_fine_grained_hash_field_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_hash_attr_fine_grained_hash_field_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'atrribute': 'SAI_HASH_ATTR_FINE_GRAINED_HASH_FIELD_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_hash_remove(self, npu):
        commands = [
            {
                'name': 'hash_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HASH',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
