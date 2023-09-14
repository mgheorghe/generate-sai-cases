
from pprint import pprint

import pytest

@pytest.mark.dpu
class TestSaiOutboundRoutingEntry:
    # object with no attributes

    def test_outbound_routing_entry_create(self, dpu):

        commands = [{'name': 'outbound_routing_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY', 'attributes': [], 'key': {'switch_id': '$SWITCH_ID', 'eni_id': 'TODO', 'destination': 'TODO'}}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_action_set")
    def test_sai_outbound_routing_entry_attr_action_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION", 'SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_action_set"])
    def test_sai_outbound_routing_entry_attr_action_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET', 'Get error, expected SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_dst_vnet_id_set")
    def test_sai_outbound_routing_entry_attr_dst_vnet_id_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID", 'SAI_NULL_OBJECT_ID']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_dst_vnet_id_set"])
    def test_sai_outbound_routing_entry_attr_dst_vnet_id_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', 'Get error, expected SAI_NULL_OBJECT_ID but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_meter_policy_en_set")
    def test_sai_outbound_routing_entry_attr_meter_policy_en_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_POLICY_EN", 'false']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_meter_policy_en_set"])
    def test_sai_outbound_routing_entry_attr_meter_policy_en_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_POLICY_EN"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_meter_class_set")
    def test_sai_outbound_routing_entry_attr_meter_class_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_CLASS", '0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_meter_class_set"])
    def test_sai_outbound_routing_entry_attr_meter_class_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_CLASS"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_overlay_ip_set")
    def test_sai_outbound_routing_entry_attr_overlay_ip_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_IP", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_overlay_ip_set"])
    def test_sai_outbound_routing_entry_attr_overlay_ip_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_IP"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_overlay_dip_set")
    def test_sai_outbound_routing_entry_attr_overlay_dip_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_overlay_dip_set"])
    def test_sai_outbound_routing_entry_attr_overlay_dip_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_overlay_dip_mask_set")
    def test_sai_outbound_routing_entry_attr_overlay_dip_mask_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP_MASK", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_overlay_dip_mask_set"])
    def test_sai_outbound_routing_entry_attr_overlay_dip_mask_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_DIP_MASK"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_overlay_sip_set")
    def test_sai_outbound_routing_entry_attr_overlay_sip_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_overlay_sip_set"])
    def test_sai_outbound_routing_entry_attr_overlay_sip_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_overlay_sip_mask_set")
    def test_sai_outbound_routing_entry_attr_overlay_sip_mask_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP_MASK", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_overlay_sip_mask_set"])
    def test_sai_outbound_routing_entry_attr_overlay_sip_mask_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_OVERLAY_SIP_MASK"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_underlay_dip_set")
    def test_sai_outbound_routing_entry_attr_underlay_dip_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_DIP", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_underlay_dip_set"])
    def test_sai_outbound_routing_entry_attr_underlay_dip_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_DIP"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_underlay_sip_set")
    def test_sai_outbound_routing_entry_attr_underlay_sip_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_SIP", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_underlay_sip_set"])
    def test_sai_outbound_routing_entry_attr_underlay_sip_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_UNDERLAY_SIP"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0.0.0.0', 'Get error, expected 0.0.0.0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_dash_encapsulation_set")
    def test_sai_outbound_routing_entry_attr_dash_encapsulation_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DASH_ENCAPSULATION", 'SAI_DASH_ENCAPSULATION_VXLAN']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_dash_encapsulation_set"])
    def test_sai_outbound_routing_entry_attr_dash_encapsulation_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DASH_ENCAPSULATION"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_DASH_ENCAPSULATION_VXLAN', 'Get error, expected SAI_DASH_ENCAPSULATION_VXLAN but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_tunnel_key_set")
    def test_sai_outbound_routing_entry_attr_tunnel_key_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_TUNNEL_KEY", '0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_tunnel_key_set"])
    def test_sai_outbound_routing_entry_attr_tunnel_key_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_TUNNEL_KEY"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_routing_entry_attr_counter_id_set")
    def test_sai_outbound_routing_entry_attr_counter_id_set(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_COUNTER_ID", 'SAI_NULL_OBJECT_ID']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_routing_entry_attr_counter_id_set"])
    def test_sai_outbound_routing_entry_attr_counter_id_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_COUNTER_ID"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', 'Get error, expected SAI_NULL_OBJECT_ID but got %s' %  r_value


    
    def test_sai_outbound_routing_entry_attr_ip_addr_family_get(self, dpu):

        commands = [
            {
                "name": "outbound_routing_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_ROUTING_ENTRY_ATTR_IP_ADDR_FAMILY"]
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


    def test_outbound_routing_entry_remove(self, dpu):

        commands = [{'name': 'outbound_routing_entry_1', 'key': {'switch_id': '$SWITCH_ID', 'eni_id': 'TODO', 'destination': 'TODO'}, 'op': 'remove'}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

