from pprint import pprint

import pytest


class TestSaiHostifTrap:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_hostif_trap_create(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'sai_hostif_trap_type_t',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'sai_packet_action_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_hostif_trap_remove(self, npu):
        commands = [
            {
                'name': 'hostif_trap_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_TRAP',
                'attributes': [
                    'SAI_HOSTIF_TRAP_ATTR_TRAP_TYPE',
                    'sai_hostif_trap_type_t',
                    'SAI_HOSTIF_TRAP_ATTR_PACKET_ACTION',
                    'sai_packet_action_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
