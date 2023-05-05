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

    @pytest.mark.dependency(name='test_sai_acl_counter_attr_packets_set')
    def test_sai_acl_counter_attr_packets_set(self, npu):
        commands = [
            {
                'name': 'acl_counter_1',
                'op': 'set',
                'attributes': ['SAI_ACL_COUNTER_ATTR_PACKETS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_acl_counter_attr_packets_set'])
    def test_sai_acl_counter_attr_packets_get(self, npu):
        commands = [
            {
                'name': 'acl_counter_1',
                'op': 'get',
                'attributes': ['SAI_ACL_COUNTER_ATTR_PACKETS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_acl_counter_attr_bytes_set')
    def test_sai_acl_counter_attr_bytes_set(self, npu):
        commands = [
            {
                'name': 'acl_counter_1',
                'op': 'set',
                'attributes': ['SAI_ACL_COUNTER_ATTR_BYTES', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_acl_counter_attr_bytes_set'])
    def test_sai_acl_counter_attr_bytes_get(self, npu):
        commands = [
            {
                'name': 'acl_counter_1',
                'op': 'get',
                'attributes': ['SAI_ACL_COUNTER_ATTR_BYTES'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_acl_counter_attr_label_set')
    def test_sai_acl_counter_attr_label_set(self, npu):
        commands = [
            {
                'name': 'acl_counter_1',
                'op': 'set',
                'attributes': ['SAI_ACL_COUNTER_ATTR_LABEL', '""'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_acl_counter_attr_label_set'])
    def test_sai_acl_counter_attr_label_get(self, npu):
        commands = [
            {
                'name': 'acl_counter_1',
                'op': 'get',
                'attributes': ['SAI_ACL_COUNTER_ATTR_LABEL'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '""', 'Get error, expected "" but got %s' % r_value

    def test_acl_counter_remove(self, npu):
        commands = [
            {'name': 'acl_counter_1', 'op': 'remove'},
            {'name': 'acl_table_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
