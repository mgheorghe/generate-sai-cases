from pprint import pprint

import pytest


class TestSaiInsegEntry:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_inseg_entry_create(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_inseg_entry_attr_num_of_pop_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_num_of_pop_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': ['SAI_INSEG_ENTRY_ATTR_NUM_OF_POP', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_num_of_pop_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_num_of_pop_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_NUM_OF_POP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_packet_action_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_packet_action_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': [
                    'SAI_INSEG_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_packet_action_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_FORWARD' for result in results]
        ), 'Get error'

    def test_sai_inseg_entry_attr_trap_priority_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_trap_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': ['SAI_INSEG_ENTRY_ATTR_TRAP_PRIORITY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_trap_priority_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_trap_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_TRAP_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_next_hop_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_next_hop_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': ['SAI_INSEG_ENTRY_ATTR_NEXT_HOP_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_next_hop_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_next_hop_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_NEXT_HOP_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_psc_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_psc_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': [
                    'SAI_INSEG_ENTRY_ATTR_PSC_TYPE',
                    'SAI_INSEG_ENTRY_PSC_TYPE_ELSP',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_psc_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_psc_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_PSC_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_INSEG_ENTRY_PSC_TYPE_ELSP' for result in results]
        ), 'Get error'

    def test_sai_inseg_entry_attr_qos_tc_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_qos_tc_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': ['SAI_INSEG_ENTRY_ATTR_QOS_TC', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_qos_tc_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_qos_tc_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_QOS_TC',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_mpls_exp_to_tc_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_mpls_exp_to_tc_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': [
                    'SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_mpls_exp_to_tc_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_mpls_exp_to_tc_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_TC_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_mpls_exp_to_color_map_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_mpls_exp_to_color_map_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': [
                    'SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_mpls_exp_to_color_map_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_mpls_exp_to_color_map_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_COLOR_MAP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_pop_ttl_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_pop_ttl_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': [
                    'SAI_INSEG_ENTRY_ATTR_POP_TTL_MODE',
                    'SAI_INSEG_ENTRY_POP_TTL_MODE_UNIFORM',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_pop_ttl_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_pop_ttl_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_POP_TTL_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_INSEG_ENTRY_POP_TTL_MODE_UNIFORM' for result in results]
        ), 'Get error'

    def test_sai_inseg_entry_attr_pop_qos_mode_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_pop_qos_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': [
                    'SAI_INSEG_ENTRY_ATTR_POP_QOS_MODE',
                    'SAI_INSEG_ENTRY_POP_QOS_MODE_UNIFORM',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_pop_qos_mode_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_pop_qos_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_POP_QOS_MODE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_INSEG_ENTRY_POP_QOS_MODE_UNIFORM' for result in results]
        ), 'Get error'

    def test_sai_inseg_entry_attr_counter_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_counter_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': ['SAI_INSEG_ENTRY_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_inseg_entry_attr_counter_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_inseg_entry_attr_counter_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'atrribute': 'SAI_INSEG_ENTRY_ATTR_COUNTER_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_inseg_entry_remove(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
