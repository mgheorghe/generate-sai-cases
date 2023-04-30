from pprint import pprint

import pytest


class TestSaiAclCounter:
    # object with parent SAI_OBJECT_TYPE_ACL_TABLE

    def test_acl_counter_create(self, npu):
        commands = [
            {
                'name': 'acl_table_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS'],
            },
            {
                'name': 'acl_counter_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'attributes': ['SAI_ACL_COUNTER_ATTR_TABLE_ID', '$acl_table_1'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_acl_counter_attr_packets_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_counter_attr_packets_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'atrribute': ['SAI_ACL_COUNTER_ATTR_PACKETS', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_counter_attr_packets_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_counter_attr_packets_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'atrribute': 'SAI_ACL_COUNTER_ATTR_PACKETS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_acl_counter_attr_bytes_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_counter_attr_bytes_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'atrribute': ['SAI_ACL_COUNTER_ATTR_BYTES', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_counter_attr_bytes_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_counter_attr_bytes_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'atrribute': 'SAI_ACL_COUNTER_ATTR_BYTES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_acl_counter_attr_label_set(self, npu):
        commands = [
            {
                'name': 'sai_acl_counter_attr_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'atrribute': ['SAI_ACL_COUNTER_ATTR_LABEL', '""'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_acl_counter_attr_label_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_counter_attr_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'atrribute': 'SAI_ACL_COUNTER_ATTR_LABEL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '""' for result in results]), 'Get error'

    def test_acl_counter_remove(self, npu):
        commands = [
            {
                'name': 'acl_counter_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ACL_COUNTER',
                'attributes': ['SAI_ACL_COUNTER_ATTR_TABLE_ID', '$acl_table_1'],
            },
            {
                'name': 'acl_table_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
