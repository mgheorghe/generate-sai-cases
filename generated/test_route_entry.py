
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiRouteEntry:
    # object with no attributes

    def test_route_entry_create(self, npu):

        commands = [{'name': 'route_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_ROUTE_ENTRY', 'attributes': [], 'key': {'switch_id': '$SWITCH_ID', 'vr_id': 'TODO', 'destination': 'TODO'}}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_route_entry_attr_packet_action_set")
    def test_sai_route_entry_attr_packet_action_set(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "set",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_PACKET_ACTION", 'SAI_PACKET_ACTION_FORWARD']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_route_entry_attr_packet_action_set"])
    def test_sai_route_entry_attr_packet_action_get(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "get",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_PACKET_ACTION"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_PACKET_ACTION_FORWARD', 'Get error, expected SAI_PACKET_ACTION_FORWARD but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_route_entry_attr_user_trap_id_set")
    def test_sai_route_entry_attr_user_trap_id_set(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "set",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_USER_TRAP_ID", 'null']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_route_entry_attr_user_trap_id_set"])
    def test_sai_route_entry_attr_user_trap_id_get(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "get",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_USER_TRAP_ID"]
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


    @pytest.mark.dependency(name="test_sai_route_entry_attr_next_hop_id_set")
    def test_sai_route_entry_attr_next_hop_id_set(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "set",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_NEXT_HOP_ID", 'null']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_route_entry_attr_next_hop_id_set"])
    def test_sai_route_entry_attr_next_hop_id_get(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "get",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_NEXT_HOP_ID"]
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


    @pytest.mark.dependency(name="test_sai_route_entry_attr_meta_data_set")
    def test_sai_route_entry_attr_meta_data_set(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "set",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_META_DATA", '0']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_route_entry_attr_meta_data_set"])
    def test_sai_route_entry_attr_meta_data_get(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "get",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_META_DATA"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' %  r_value


    
    def test_sai_route_entry_attr_ip_addr_family_get(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "get",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_IP_ADDR_FAMILY"]
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


    @pytest.mark.dependency(name="test_sai_route_entry_attr_counter_id_set")
    def test_sai_route_entry_attr_counter_id_set(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "set",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_COUNTER_ID", 'null']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_route_entry_attr_counter_id_set"])
    def test_sai_route_entry_attr_counter_id_get(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "get",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_COUNTER_ID"]
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


    @pytest.mark.dependency(name="test_sai_route_entry_attr_prefix_agg_id_set")
    def test_sai_route_entry_attr_prefix_agg_id_set(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "set",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_PREFIX_AGG_ID", '0']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_route_entry_attr_prefix_agg_id_set"])
    def test_sai_route_entry_attr_prefix_agg_id_get(self, npu):

        commands = [
            {
                "name": "route_entry_1",
                "op": "get",
                "attributes": ["SAI_ROUTE_ENTRY_ATTR_PREFIX_AGG_ID"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' %  r_value


    def test_route_entry_remove(self, npu):

        commands = [{'name': 'route_entry_1', 'key': {'switch_id': '$SWITCH_ID', 'vr_id': 'TODO', 'destination': 'TODO'}, 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

