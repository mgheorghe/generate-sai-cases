
from pprint import pprint

import pytest

@pytest.mark.dpu
class TestSaiOutboundCaToPaEntry:
    # object with no attributes

    def test_outbound_ca_to_pa_entry_create(self, dpu):

        commands = [{'name': 'outbound_ca_to_pa_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY', 'attributes': [], 'key': {'switch_id': '$SWITCH_ID', 'dst_vnet_id': 'TODO', 'dip': 'TODO'}}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_set")
    def test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_set(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP", '0.0.0.0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_set"])
    def test_sai_outbound_ca_to_pa_entry_attr_underlay_dip_get(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP"]
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


    @pytest.mark.dependency(name="test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set")
    def test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC", '0:0:0:0:0:0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_set"])
    def test_sai_outbound_ca_to_pa_entry_attr_overlay_dmac_get(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC"]
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0:0:0:0:0:0', 'Get error, expected 0:0:0:0:0:0 but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set")
    def test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI", 'false']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_set"])
    def test_sai_outbound_ca_to_pa_entry_attr_use_dst_vnet_vni_get(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI"]
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


    @pytest.mark.dependency(name="test_sai_outbound_ca_to_pa_entry_attr_meter_class_set")
    def test_sai_outbound_ca_to_pa_entry_attr_meter_class_set(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS", '0']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_ca_to_pa_entry_attr_meter_class_set"])
    def test_sai_outbound_ca_to_pa_entry_attr_meter_class_get(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS"]
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


    @pytest.mark.dependency(name="test_sai_outbound_ca_to_pa_entry_attr_meter_class_override_set")
    def test_sai_outbound_ca_to_pa_entry_attr_meter_class_override_set(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS_OVERRIDE", 'false']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_ca_to_pa_entry_attr_meter_class_override_set"])
    def test_sai_outbound_ca_to_pa_entry_attr_meter_class_override_get(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS_OVERRIDE"]
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


    @pytest.mark.dependency(name="test_sai_outbound_ca_to_pa_entry_attr_counter_id_set")
    def test_sai_outbound_ca_to_pa_entry_attr_counter_id_set(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "set",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_COUNTER_ID", 'SAI_NULL_OBJECT_ID']
            }
        ]
        results = [*dpu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_outbound_ca_to_pa_entry_attr_counter_id_set"])
    def test_sai_outbound_ca_to_pa_entry_attr_counter_id_get(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_COUNTER_ID"]
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


    
    def test_sai_outbound_ca_to_pa_entry_attr_ip_addr_family_get(self, dpu):

        commands = [
            {
                "name": "outbound_ca_to_pa_entry_1",
                "op": "get",
                "attributes": ["SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_IP_ADDR_FAMILY"]
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


    def test_outbound_ca_to_pa_entry_remove(self, dpu):

        commands = [{'name': 'outbound_ca_to_pa_entry_1', 'key': {'switch_id': '$SWITCH_ID', 'dst_vnet_id': 'TODO', 'dip': 'TODO'}, 'op': 'remove'}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

