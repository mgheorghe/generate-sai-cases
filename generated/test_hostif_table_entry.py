from pprint import pprint


class TestSaiHostifTableEntry:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_HOSTIF_TRAP SAI_OBJECT_TYPE_HOSTIF_USER_DEFINED_TRAP SAI_OBJECT_TYPE_HOSTIF

    def test_hostif_table_entry_create(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'hostif_trap_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'SAI_HOSTIF_TRAP_TYPE_STP',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            },
            {
                'name': 'hostif_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF',
                'attributes': [
                    'SAI_HOSTIF_ATTR_TYPE',
                    'SAI_HOSTIF_TYPE_NETDEV',
                    'SAI_HOSTIF_ATTR_OBJ_ID',
                    '$port_1',
                    'SAI_HOSTIF_ATTR_NAME',
                    'char',
                    'SAI_HOSTIF_ATTR_GENETLINK_MCGRP_NAME',
                    'char',
                ],
            },
            {
                'name': 'hostif_table_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY',
                'attributes': [
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TYPE',
                    'SAI_HOSTIF_TABLE_ENTRY_TYPE_PORT',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_OBJ_ID',
                    '$port_1',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TRAP_ID',
                    '$hostif_trap_1',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_CHANNEL_TYPE',
                    'SAI_HOSTIF_TABLE_ENTRY_CHANNEL_TYPE_CB',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_HOST_IF',
                    '$hostif_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_hostif_table_entry_remove(self, npu):
        commands = [
            {
                'name': 'hostif_table_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TABLE_ENTRY',
                'attributes': [
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TYPE',
                    'SAI_HOSTIF_TABLE_ENTRY_TYPE_PORT',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_OBJ_ID',
                    '$port_1',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_TRAP_ID',
                    '$hostif_trap_1',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_CHANNEL_TYPE',
                    'SAI_HOSTIF_TABLE_ENTRY_CHANNEL_TYPE_CB',
                    'SAI_HOSTIF_TABLE_ENTRY_ATTR_HOST_IF',
                    '$hostif_1',
                ],
            },
            {
                'name': 'hostif_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF',
                'attributes': [
                    'SAI_HOSTIF_ATTR_TYPE',
                    'SAI_HOSTIF_TYPE_NETDEV',
                    'SAI_HOSTIF_ATTR_OBJ_ID',
                    '$port_1',
                    'SAI_HOSTIF_ATTR_NAME',
                    'char',
                    'SAI_HOSTIF_ATTR_GENETLINK_MCGRP_NAME',
                    'char',
                ],
            },
            {
                'name': 'hostif_trap_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'SAI_HOSTIF_TRAP_TYPE_STP',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
