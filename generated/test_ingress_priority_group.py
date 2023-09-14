
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiIngressPriorityGroup:
    # object with parent SAI_OBJECT_TYPE_PORT

    def test_ingress_priority_group_create(self, npu):

        commands = [{'name': 'port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_PORT', 'attributes': ['SAI_PORT_ATTR_HW_LANE_LIST', '2:10,11', 'SAI_PORT_ATTR_SPEED', '10']}, {'name': 'ingress_priority_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP', 'attributes': ['SAI_INGRESS_PRIORITY_GROUP_ATTR_PORT', '$port_1', 'SAI_INGRESS_PRIORITY_GROUP_ATTR_INDEX', '1']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_ingress_priority_group_attr_buffer_profile_set")
    def test_sai_ingress_priority_group_attr_buffer_profile_set(self, npu):

        commands = [
            {
                "name": "ingress_priority_group_1",
                "op": "set",
                "attributes": ["SAI_INGRESS_PRIORITY_GROUP_ATTR_BUFFER_PROFILE", 'SAI_NULL_OBJECT_ID']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_ingress_priority_group_attr_buffer_profile_set"])
    def test_sai_ingress_priority_group_attr_buffer_profile_get(self, npu):

        commands = [
            {
                "name": "ingress_priority_group_1",
                "op": "get",
                "attributes": ["SAI_INGRESS_PRIORITY_GROUP_ATTR_BUFFER_PROFILE"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NULL_OBJECT_ID', 'Get error, expected SAI_NULL_OBJECT_ID but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_ingress_priority_group_attr_tam_set")
    def test_sai_ingress_priority_group_attr_tam_set(self, npu):

        commands = [
            {
                "name": "ingress_priority_group_1",
                "op": "set",
                "attributes": ["SAI_INGRESS_PRIORITY_GROUP_ATTR_TAM", 'empty']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_ingress_priority_group_attr_tam_set"])
    def test_sai_ingress_priority_group_attr_tam_get(self, npu):

        commands = [
            {
                "name": "ingress_priority_group_1",
                "op": "get",
                "attributes": ["SAI_INGRESS_PRIORITY_GROUP_ATTR_TAM"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'empty', 'Get error, expected empty but got %s' %  r_value


    def test_ingress_priority_group_remove(self, npu):

        commands = [{'name': 'ingress_priority_group_1', 'op': 'remove'}, {'name': 'port_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

