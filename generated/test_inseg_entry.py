from pprint import pprint

import pytest


class TestSaiInsegEntry:
    # object with no attributes

    def test_inseg_entry_create(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INSEG_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'label': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_num_of_pop_set')
    def test_sai_inseg_entry_attr_num_of_pop_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_NUM_OF_POP', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_num_of_pop_set'])
    def test_sai_inseg_entry_attr_num_of_pop_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_NUM_OF_POP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_packet_action_set')
    def test_sai_inseg_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_INSEG_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_FORWARD',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_packet_action_set'])
    def test_sai_inseg_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_PACKET_ACTION'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PACKET_ACTION_FORWARD', (
            'Get error, expected SAI_PACKET_ACTION_FORWARD but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_trap_priority_set')
    def test_sai_inseg_entry_attr_trap_priority_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_TRAP_PRIORITY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_trap_priority_set'])
    def test_sai_inseg_entry_attr_trap_priority_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_TRAP_PRIORITY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_next_hop_id_set')
    def test_sai_inseg_entry_attr_next_hop_id_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_INSEG_ENTRY_ATTR_NEXT_HOP_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_next_hop_id_set'])
    def test_sai_inseg_entry_attr_next_hop_id_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_NEXT_HOP_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_psc_type_set')
    def test_sai_inseg_entry_attr_psc_type_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_INSEG_ENTRY_ATTR_PSC_TYPE',
                    'SAI_INSEG_ENTRY_PSC_TYPE_ELSP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_psc_type_set'])
    def test_sai_inseg_entry_attr_psc_type_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_PSC_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_INSEG_ENTRY_PSC_TYPE_ELSP', (
            'Get error, expected SAI_INSEG_ENTRY_PSC_TYPE_ELSP but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_qos_tc_set')
    def test_sai_inseg_entry_attr_qos_tc_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_QOS_TC', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_qos_tc_set'])
    def test_sai_inseg_entry_attr_qos_tc_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_QOS_TC'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_mpls_exp_to_tc_map_set')
    def test_sai_inseg_entry_attr_mpls_exp_to_tc_map_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_TC_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_inseg_entry_attr_mpls_exp_to_tc_map_set']
    )
    def test_sai_inseg_entry_attr_mpls_exp_to_tc_map_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_TC_MAP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_mpls_exp_to_color_map_set')
    def test_sai_inseg_entry_attr_mpls_exp_to_color_map_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_COLOR_MAP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_inseg_entry_attr_mpls_exp_to_color_map_set']
    )
    def test_sai_inseg_entry_attr_mpls_exp_to_color_map_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_MPLS_EXP_TO_COLOR_MAP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_pop_ttl_mode_set')
    def test_sai_inseg_entry_attr_pop_ttl_mode_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_INSEG_ENTRY_ATTR_POP_TTL_MODE',
                    'SAI_INSEG_ENTRY_POP_TTL_MODE_UNIFORM',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_pop_ttl_mode_set'])
    def test_sai_inseg_entry_attr_pop_ttl_mode_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_POP_TTL_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_INSEG_ENTRY_POP_TTL_MODE_UNIFORM', (
            'Get error, expected SAI_INSEG_ENTRY_POP_TTL_MODE_UNIFORM but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_pop_qos_mode_set')
    def test_sai_inseg_entry_attr_pop_qos_mode_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': [
                    'SAI_INSEG_ENTRY_ATTR_POP_QOS_MODE',
                    'SAI_INSEG_ENTRY_POP_QOS_MODE_UNIFORM',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_pop_qos_mode_set'])
    def test_sai_inseg_entry_attr_pop_qos_mode_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_POP_QOS_MODE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_INSEG_ENTRY_POP_QOS_MODE_UNIFORM', (
            'Get error, expected SAI_INSEG_ENTRY_POP_QOS_MODE_UNIFORM but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_inseg_entry_attr_counter_id_set')
    def test_sai_inseg_entry_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'set',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_COUNTER_ID', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inseg_entry_attr_counter_id_set'])
    def test_sai_inseg_entry_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'op': 'get',
                'attributes': ['SAI_INSEG_ENTRY_ATTR_COUNTER_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % r_value
        )

    def test_inseg_entry_remove(self, npu):
        commands = [
            {
                'name': 'inseg_entry_1',
                'key': {'switch_id': '$SWITCH_ID', 'label': 'TODO'},
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
