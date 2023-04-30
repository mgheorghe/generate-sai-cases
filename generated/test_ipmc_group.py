from pprint import pprint

import pytest


class TestSaiIpmcGroup:
    # object with no attributes

    def test_ipmc_group_create(self, npu):
        commands = [
            {
                'name': 'ipmc_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_ipmc_group_attr_ipmc_output_count_get(self, npu):
        commands = [
            {
                'name': 'sai_ipmc_group_attr_ipmc_output_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP',
                'atrribute': 'SAI_IPMC_GROUP_ATTR_IPMC_OUTPUT_COUNT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ipmc_group_attr_ipmc_member_list_get(self, npu):
        commands = [
            {
                'name': 'sai_ipmc_group_attr_ipmc_member_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP',
                'atrribute': 'SAI_IPMC_GROUP_ATTR_IPMC_MEMBER_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_ipmc_group_remove(self, npu):
        commands = [
            {
                'name': 'ipmc_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPMC_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
