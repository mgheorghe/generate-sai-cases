
from pprint import pprint

import pytest

@pytest.mark.dpu
class TestSaiInboundRoutingEntry:
    # object with no attributes

    def test_inbound_routing_entry_create(self, dpu):

        commands = [{'name': 'inbound_routing_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY', 'attributes': [], 'key': {'switch_id': '$SWITCH_ID', 'eni_id': 'TODO', 'vni': 'TODO', 'sip': 'TODO', 'sip_mask': 'TODO', 'priority': 'TODO'}}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_inbound_routing_entry_attr_action_set")
    def test_sai_inbound_routing_entry_attr_action_set(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION", 'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_inbound_routing_entry_attr_action_set"])
    def test_sai_inbound_routing_entry_attr_action_get(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP', 'Get error, expected SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_inbound_routing_entry_attr_src_vnet_id_set")
    def test_sai_inbound_routing_entry_attr_src_vnet_id_set(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID", 'null']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_inbound_routing_entry_attr_src_vnet_id_set"])
    def test_sai_inbound_routing_entry_attr_src_vnet_id_get(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' %  r_value


    
    def test_sai_inbound_routing_entry_attr_ip_addr_family_get(self, dpu):

        commands = [
            {
                "name": "inbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_INBOUND_ROUTING_ENTRY_ATTR_IP_ADDR_FAMILY"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    def test_inbound_routing_entry_remove(self, dpu):

        commands = [{'name': 'inbound_routing_entry_1', 'key': {'switch_id': '$SWITCH_ID', 'eni_id': 'TODO', 'vni': 'TODO', 'sip': 'TODO', 'sip_mask': 'TODO', 'priority': 'TODO'}, 'op': 'remove'}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

