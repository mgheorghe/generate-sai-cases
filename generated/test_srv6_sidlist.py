from pprint import pprint

import pytest


class TestSaiSrv6Sidlist:
    # object with no parents

    def test_srv6_sidlist_create(self, npu):
        commands = [
            {
                'name': 'srv6_sidlist_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_srv6_sidlist_attr_tlv_list_set(self, npu):
        commands = [
            {
                'name': 'sai_srv6_sidlist_attr_tlv_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'atrribute': ['SAI_SRV6_SIDLIST_ATTR_TLV_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_srv6_sidlist_attr_tlv_list_get(self, npu):
        commands = [
            {
                'name': 'sai_srv6_sidlist_attr_tlv_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'atrribute': 'SAI_SRV6_SIDLIST_ATTR_TLV_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_srv6_sidlist_attr_segment_list_set(self, npu):
        commands = [
            {
                'name': 'sai_srv6_sidlist_attr_segment_list_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'atrribute': ['SAI_SRV6_SIDLIST_ATTR_SEGMENT_LIST', 'empty'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_srv6_sidlist_attr_segment_list_get(self, npu):
        commands = [
            {
                'name': 'sai_srv6_sidlist_attr_segment_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'atrribute': 'SAI_SRV6_SIDLIST_ATTR_SEGMENT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'empty' for result in results]), 'Get error'

    def test_sai_srv6_sidlist_attr_next_hop_id_set(self, npu):
        commands = [
            {
                'name': 'sai_srv6_sidlist_attr_next_hop_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'atrribute': [
                    'SAI_SRV6_SIDLIST_ATTR_NEXT_HOP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_srv6_sidlist_attr_next_hop_id_get(self, npu):
        commands = [
            {
                'name': 'sai_srv6_sidlist_attr_next_hop_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'atrribute': 'SAI_SRV6_SIDLIST_ATTR_NEXT_HOP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_srv6_sidlist_remove(self, npu):
        commands = [
            {
                'name': 'srv6_sidlist_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SRV6_SIDLIST',
                'attributes': ['SAI_SRV6_SIDLIST_ATTR_TYPE', 'sai_srv6_sidlist_type_t'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
