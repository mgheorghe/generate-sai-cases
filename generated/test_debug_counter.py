
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiDebugCounter:
    # object with no parents

    def test_debug_counter_create(self, npu):

        commands = [{'name': 'debug_counter_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER', 'attributes': ['SAI_DEBUG_COUNTER_ATTR_TYPE', 'SAI_DEBUG_COUNTER_TYPE_PORT_IN_DROP_REASONS']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_debug_counter_attr_index_get(self, npu):

        commands = [
            {
                "name": "debug_counter_1",
                "op": "get",
                "attributes": ["SAI_DEBUG_COUNTER_ATTR_INDEX"]
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


    @pytest.mark.dependency(name="test_sai_debug_counter_attr_in_drop_reason_list_set")
    def test_sai_debug_counter_attr_in_drop_reason_list_set(self, npu):

        commands = [
            {
                "name": "debug_counter_1",
                "op": "set",
                "attributes": ["SAI_DEBUG_COUNTER_ATTR_IN_DROP_REASON_LIST", 'empty']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_debug_counter_attr_in_drop_reason_list_set"])
    def test_sai_debug_counter_attr_in_drop_reason_list_get(self, npu):

        commands = [
            {
                "name": "debug_counter_1",
                "op": "get",
                "attributes": ["SAI_DEBUG_COUNTER_ATTR_IN_DROP_REASON_LIST"]
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


    @pytest.mark.dependency(name="test_sai_debug_counter_attr_out_drop_reason_list_set")
    def test_sai_debug_counter_attr_out_drop_reason_list_set(self, npu):

        commands = [
            {
                "name": "debug_counter_1",
                "op": "set",
                "attributes": ["SAI_DEBUG_COUNTER_ATTR_OUT_DROP_REASON_LIST", 'empty']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_debug_counter_attr_out_drop_reason_list_set"])
    def test_sai_debug_counter_attr_out_drop_reason_list_get(self, npu):

        commands = [
            {
                "name": "debug_counter_1",
                "op": "get",
                "attributes": ["SAI_DEBUG_COUNTER_ATTR_OUT_DROP_REASON_LIST"]
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


    def test_debug_counter_remove(self, npu):

        commands = [{'name': 'debug_counter_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

