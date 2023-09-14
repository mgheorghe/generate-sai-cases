
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiSchedulerGroup:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SCHEDULER_GROUP SAI_OBJECT_TYPE_PORT

    def test_scheduler_group_create(self, npu):

        commands = [{'name': 'port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_PORT', 'attributes': ['SAI_PORT_ATTR_HW_LANE_LIST', '2:10,11', 'SAI_PORT_ATTR_SPEED', '10']}, {'name': 'scheduler_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP', 'attributes': ['SAI_SCHEDULER_GROUP_ATTR_PORT_ID', '$port_1', 'SAI_SCHEDULER_GROUP_ATTR_LEVEL', '1', 'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS', '1', 'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE', 'TODO_circular parent reference']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_scheduler_group_attr_child_count_get(self, npu):

        commands = [
            {
                "name": "scheduler_group_1",
                "op": "get",
                "attributes": ["SAI_SCHEDULER_GROUP_ATTR_CHILD_COUNT"]
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


    
    def test_sai_scheduler_group_attr_child_list_get(self, npu):

        commands = [
            {
                "name": "scheduler_group_1",
                "op": "get",
                "attributes": ["SAI_SCHEDULER_GROUP_ATTR_CHILD_LIST"]
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


    @pytest.mark.dependency(name="test_sai_scheduler_group_attr_scheduler_profile_id_set")
    def test_sai_scheduler_group_attr_scheduler_profile_id_set(self, npu):

        commands = [
            {
                "name": "scheduler_group_1",
                "op": "set",
                "attributes": ["SAI_SCHEDULER_GROUP_ATTR_SCHEDULER_PROFILE_ID", 'SAI_NULL_OBJECT_ID']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_scheduler_group_attr_scheduler_profile_id_set"])
    def test_sai_scheduler_group_attr_scheduler_profile_id_get(self, npu):

        commands = [
            {
                "name": "scheduler_group_1",
                "op": "get",
                "attributes": ["SAI_SCHEDULER_GROUP_ATTR_SCHEDULER_PROFILE_ID"]
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


    @pytest.mark.dependency(name="test_sai_scheduler_group_attr_parent_node_set")
    def test_sai_scheduler_group_attr_parent_node_set(self, npu):

        commands = [
            {
                "name": "scheduler_group_1",
                "op": "set",
                "attributes": ["SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE", 'TODO']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_scheduler_group_attr_parent_node_set"])
    def test_sai_scheduler_group_attr_parent_node_get(self, npu):

        commands = [
            {
                "name": "scheduler_group_1",
                "op": "get",
                "attributes": ["SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE"]
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


    def test_scheduler_group_remove(self, npu):

        commands = [{'name': 'scheduler_group_1', 'op': 'remove'}, {'name': 'port_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

