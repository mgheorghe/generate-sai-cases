from pprint import pprint

import pytest


class TestSaiInboundRoutingEntry:
    # object with no attributes

    def test_inbound_routing_entry_create(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'attributes': [],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'eni_id': 'TODO',
                    'vni': 'TODO',
                    'sip': 'TODO',
                    'sip_mask': 'TODO',
                    'priority': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_inbound_routing_entry_attr_action_set(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION',
                    'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_inbound_routing_entry_attr_action_set'])
    def test_sai_inbound_routing_entry_attr_action_get(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert (
            results[1][0].value() == 'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP'
        ), (
            'Get error, expected SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP but got %s'
            % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_inbound_routing_entry_attr_src_vnet_id_set(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': [
                    'SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_inbound_routing_entry_attr_src_vnet_id_set']
    )
    def test_sai_inbound_routing_entry_attr_src_vnet_id_get(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'atrribute': 'SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_inbound_routing_entry_remove(self, npu):
        commands = [
            {
                'name': 'inbound_routing_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY',
                'attributes': [],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'eni_id': 'TODO',
                    'vni': 'TODO',
                    'sip': 'TODO',
                    'sip_mask': 'TODO',
                    'priority': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
