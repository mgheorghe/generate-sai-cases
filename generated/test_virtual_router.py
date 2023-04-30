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

    def test_sai_virtual_router_attr_admin_v4_state_set(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_admin_v4_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': ['SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_admin_v4_state_get(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_admin_v4_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V4_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_admin_v6_state_set(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_admin_v6_state_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': ['SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_admin_v6_state_get(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_admin_v6_state_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_ADMIN_V6_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_src_mac_address_set(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_src_mac_address_set',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_src_mac_address_get(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_src_mac_address_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_SRC_MAC_ADDRESS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [
                result == 'attrvalue SAI_SWITCH_ATTR_SRC_MAC_ADDRESS'
                for result in results
            ]
        ), 'Get error'

    def test_sai_virtual_router_attr_violation_ttl1_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_violation_ttl1_packet_action_set',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_violation_ttl1_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_violation_ttl1_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_TTL1_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_TRAP' for result in results]
        ), 'Get error'

    def test_sai_virtual_router_attr_violation_ip_options_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_violation_ip_options_packet_action_set',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_violation_ip_options_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_violation_ip_options_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_VIOLATION_IP_OPTIONS_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_TRAP' for result in results]
        ), 'Get error'

    def test_sai_virtual_router_attr_unknown_l3_multicast_packet_action_set(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_unknown_l3_multicast_packet_action_set',
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_unknown_l3_multicast_packet_action_get(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_unknown_l3_multicast_packet_action_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_UNKNOWN_L3_MULTICAST_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_PACKET_ACTION_DROP' for result in results]
        ), 'Get error'

    def test_sai_virtual_router_attr_label_set(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_label_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': ['SAI_VIRTUAL_ROUTER_ATTR_LABEL', '""'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_virtual_router_attr_label_get(self, npu):
        commands = [
            {
                'name': 'sai_virtual_router_attr_label_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'atrribute': 'SAI_VIRTUAL_ROUTER_ATTR_LABEL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '""' for result in results]), 'Get error'

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
