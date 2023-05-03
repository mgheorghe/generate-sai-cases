from pprint import pprint

import pytest


class TestSaiVirtualRouter:
    # object with no attributes

    def test_virtual_router_create(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_virtual_router_attr_admin_v4_state_set(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': ['SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_virtual_router_attr_admin_v4_state_set'])
    def test_sai_virtual_router_attr_admin_v4_state_get(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'true', (
            'Get error, expected true but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_virtual_router_attr_admin_v6_state_set(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': ['SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_virtual_router_attr_admin_v6_state_set'])
    def test_sai_virtual_router_attr_admin_v6_state_get(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'true', (
            'Get error, expected true but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_virtual_router_attr_src_mac_address_set(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': [
                    'SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS',
                    'attrvalue SAI_SWITCH_ATTR_SRC_MAC_ADDRESS',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_virtual_router_attr_src_mac_address_set']
    )
    def test_sai_virtual_router_attr_src_mac_address_get(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'attrvalue SAI_SWITCH_ATTR_SRC_MAC_ADDRESS', (
            'Get error, expected attrvalue SAI_SWITCH_ATTR_SRC_MAC_ADDRESS but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_virtual_router_attr_violation_ttl1_packet_action_set(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': [
                    'SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_TTL1_PACKET_ACTION',
                    'SAI_PACKET_ACTION_TRAP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_virtual_router_attr_violation_ttl1_packet_action_set']
    )
    def test_sai_virtual_router_attr_violation_ttl1_packet_action_get(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_TTL1_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_PACKET_ACTION_TRAP', (
            'Get error, expected SAI_PACKET_ACTION_TRAP but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_virtual_router_attr_violation_ip_options_packet_action_set(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': [
                    'SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_IP_OPTIONS_PACKET_ACTION',
                    'SAI_PACKET_ACTION_TRAP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_virtual_router_attr_violation_ip_options_packet_action_set']
    )
    def test_sai_virtual_router_attr_violation_ip_options_packet_action_get(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_IP_OPTIONS_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_PACKET_ACTION_TRAP', (
            'Get error, expected SAI_PACKET_ACTION_TRAP but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_virtual_router_attr_unknown_l3_multicast_packet_action_set(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': [
                    'SAI_VIRTUAL_ROUTER_ATTR_UNKNOWN_L3_MULTICAST_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_virtual_router_attr_unknown_l3_multicast_packet_action_set']
    )
    def test_sai_virtual_router_attr_unknown_l3_multicast_packet_action_get(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_UNKNOWN_L3_MULTICAST_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_PACKET_ACTION_DROP', (
            'Get error, expected SAI_PACKET_ACTION_DROP but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_virtual_router_attr_label_set(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': ['SAI_VIRTUAL_ROUTER_ATTR_LABEL', '""'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_virtual_router_attr_label_set'])
    def test_sai_virtual_router_attr_label_get(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_LABEL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '""', (
            'Get error, expected "" but got %s' % results[1][0].value()
        )

    def test_virtual_router_remove(self, npu):
        commands = [
            {
                'name': 'virtual_router_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
