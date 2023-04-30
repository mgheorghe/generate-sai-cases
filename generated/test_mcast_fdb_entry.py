from pprint import pprint

import pytest


class TestSaiMcastFdbEntry:
    # object with parent SAI_OBJECT_TYPE_L2MC_GROUP

    def test_mcast_fdb_entry_create(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            },
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'attributes': [
                    'SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID',
                    '$l2mc_group_1',
                    'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_mcast_fdb_entry_attr_group_id_set(self, npu):
        commands = [
            {
                'name': 'sai_mcast_fdb_entry_attr_group_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': ['SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mcast_fdb_entry_attr_group_id_get(self, npu):
        commands = [
            {
                'name': 'sai_mcast_fdb_entry_attr_group_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': 'SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mcast_fdb_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_mcast_fdb_entry_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': ['SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mcast_fdb_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_mcast_fdb_entry_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': 'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_mcast_fdb_entry_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'sai_mcast_fdb_entry_attr_meta_data_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': ['SAI_MCAST_FDB_ENTRY_ATTR_META_DATA', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_mcast_fdb_entry_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'sai_mcast_fdb_entry_attr_meta_data_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': 'SAI_MCAST_FDB_ENTRY_ATTR_META_DATA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_mcast_fdb_entry_remove(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'attributes': [
                    'SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID',
                    '$l2mc_group_1',
                    'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            },
            {
                'name': 'l2mc_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
