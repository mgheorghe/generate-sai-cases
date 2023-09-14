
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiSystemPort:
    # object with no parents

    def test_system_port_create(self, npu):

        commands = [{'name': 'system_port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT', 'attributes': ['SAI_SYSTEM_PORT_ATTR_CONFIG_INFO', 'TODO']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_system_port_attr_type_get(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "get",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_TYPE"]
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


    
    def test_sai_system_port_attr_qos_number_of_voqs_get(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "get",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_QOS_NUMBER_OF_VOQS"]
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


    
    def test_sai_system_port_attr_qos_voq_list_get(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "get",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_QOS_VOQ_LIST"]
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


    
    def test_sai_system_port_attr_port_get(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "get",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_PORT"]
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


    @pytest.mark.dependency(name="test_sai_system_port_attr_admin_state_set")
    def test_sai_system_port_attr_admin_state_set(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "set",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_ADMIN_STATE", 'false']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_system_port_attr_admin_state_set"])
    def test_sai_system_port_attr_admin_state_get(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "get",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_ADMIN_STATE"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_system_port_attr_qos_tc_to_queue_map_set")
    def test_sai_system_port_attr_qos_tc_to_queue_map_set(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "set",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_QOS_TC_TO_QUEUE_MAP", 'null']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_system_port_attr_qos_tc_to_queue_map_set"])
    def test_sai_system_port_attr_qos_tc_to_queue_map_get(self, npu):

        commands = [
            {
                "name": "system_port_1",
                "op": "get",
                "attributes": ["SAI_SYSTEM_PORT_ATTR_QOS_TC_TO_QUEUE_MAP"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' %  r_value


    def test_system_port_remove(self, npu):

        commands = [{'name': 'system_port_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

