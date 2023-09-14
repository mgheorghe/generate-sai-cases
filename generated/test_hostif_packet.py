
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiHostifPacket:
    # object with parent SAI_OBJECT_TYPE_PORT

    def test_hostif_packet_create(self, npu):

        commands = [{'name': 'port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_PORT', 'attributes': ['SAI_PORT_ATTR_HW_LANE_LIST', '2:10,11', 'SAI_PORT_ATTR_SPEED', '10']}, {'name': 'hostif_packet_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HOSTIF_PACKET', 'attributes': ['SAI_HOSTIF_PACKET_ATTR_HOSTIF_TX_TYPE', 'SAI_HOSTIF_TX_TYPE_PIPELINE_BYPASS', 'SAI_HOSTIF_PACKET_ATTR_EGRESS_PORT_OR_LAG', '$port_1']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_hostif_packet_attr_hostif_trap_id_get(self, npu):

        commands = [
            {
                "name": "hostif_packet_1",
                "op": "get",
                "attributes": ["SAI_HOSTIF_PACKET_ATTR_HOSTIF_TRAP_ID"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    
    def test_sai_hostif_packet_attr_ingress_port_get(self, npu):

        commands = [
            {
                "name": "hostif_packet_1",
                "op": "get",
                "attributes": ["SAI_HOSTIF_PACKET_ATTR_INGRESS_PORT"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    
    def test_sai_hostif_packet_attr_ingress_lag_get(self, npu):

        commands = [
            {
                "name": "hostif_packet_1",
                "op": "get",
                "attributes": ["SAI_HOSTIF_PACKET_ATTR_INGRESS_LAG"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    
    def test_sai_hostif_packet_attr_bridge_id_get(self, npu):

        commands = [
            {
                "name": "hostif_packet_1",
                "op": "get",
                "attributes": ["SAI_HOSTIF_PACKET_ATTR_BRIDGE_ID"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    
    def test_sai_hostif_packet_attr_timestamp_get(self, npu):

        commands = [
            {
                "name": "hostif_packet_1",
                "op": "get",
                "attributes": ["SAI_HOSTIF_PACKET_ATTR_TIMESTAMP"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    def test_hostif_packet_remove(self, npu):

        commands = [{'name': 'hostif_packet_1', 'op': 'remove'}, {'name': 'port_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

