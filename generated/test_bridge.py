from pprint import pprint

import pytest


class TestSaiBridge:
    # object with no parents

    def test_bridge_create(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_bridge_attr_port_list_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_PORT_LIST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bridge_attr_max_learned_addresses_set')
    def test_sai_bridge_attr_max_learned_addresses_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': ['SAI_BRIDGE_ATTR_MAX_LEARNED_ADDRESSES', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bridge_attr_max_learned_addresses_set'])
    def test_sai_bridge_attr_max_learned_addresses_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_MAX_LEARNED_ADDRESSES'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_bridge_attr_learn_disable_set')
    def test_sai_bridge_attr_learn_disable_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': ['SAI_BRIDGE_ATTR_LEARN_DISABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bridge_attr_learn_disable_set'])
    def test_sai_bridge_attr_learn_disable_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_LEARN_DISABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(
        name='test_sai_bridge_attr_unknown_unicast_flood_control_type_set'
    )
    def test_sai_bridge_attr_unknown_unicast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE',
                    'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_bridge_attr_unknown_unicast_flood_control_type_set']
    )
    def test_sai_bridge_attr_unknown_unicast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS', (
            'Get error, expected SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_bridge_attr_unknown_unicast_flood_group_set')
    def test_sai_bridge_attr_unknown_unicast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_bridge_attr_unknown_unicast_flood_group_set']
    )
    def test_sai_bridge_attr_unknown_unicast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP'],
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

    @pytest.mark.dependency(
        name='test_sai_bridge_attr_unknown_multicast_flood_control_type_set'
    )
    def test_sai_bridge_attr_unknown_multicast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE',
                    'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_bridge_attr_unknown_multicast_flood_control_type_set']
    )
    def test_sai_bridge_attr_unknown_multicast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS', (
            'Get error, expected SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS but got %s'
            % r_value
        )

    @pytest.mark.dependency(
        name='test_sai_bridge_attr_unknown_multicast_flood_group_set'
    )
    def test_sai_bridge_attr_unknown_multicast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_bridge_attr_unknown_multicast_flood_group_set']
    )
    def test_sai_bridge_attr_unknown_multicast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP'],
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

    @pytest.mark.dependency(
        name='test_sai_bridge_attr_broadcast_flood_control_type_set'
    )
    def test_sai_bridge_attr_broadcast_flood_control_type_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': [
                    'SAI_BRIDGE_ATTR_BROADCAST_FLOOD_CONTROL_TYPE',
                    'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_bridge_attr_broadcast_flood_control_type_set']
    )
    def test_sai_bridge_attr_broadcast_flood_control_type_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_BROADCAST_FLOOD_CONTROL_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS', (
            'Get error, expected SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS but got %s'
            % r_value
        )

    @pytest.mark.dependency(name='test_sai_bridge_attr_broadcast_flood_group_set')
    def test_sai_bridge_attr_broadcast_flood_group_set(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'set',
                'attributes': [
                    'SAI_BRIDGE_ATTR_BROADCAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_bridge_attr_broadcast_flood_group_set'])
    def test_sai_bridge_attr_broadcast_flood_group_get(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'get',
                'attributes': ['SAI_BRIDGE_ATTR_BROADCAST_FLOOD_GROUP'],
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

    def test_bridge_remove(self, npu):
        commands = [{'name': 'bridge_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
