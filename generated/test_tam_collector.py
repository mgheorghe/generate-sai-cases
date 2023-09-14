
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiTamCollector:
    # object with parent SAI_OBJECT_TYPE_TAM_TRANSPORT

    def test_tam_collector_create(self, npu):

        commands = [{'name': 'tam_transport_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_TRANSPORT', 'attributes': ['SAI_TAM_TRANSPORT_ATTR_TRANSPORT_TYPE', 'SAI_TAM_TRANSPORT_TYPE_TCP']}, {'name': 'tam_collector_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_COLLECTOR', 'attributes': ['SAI_TAM_COLLECTOR_ATTR_SRC_IP', '180.0.0.1', 'SAI_TAM_COLLECTOR_ATTR_DST_IP', '180.0.0.1', 'SAI_TAM_COLLECTOR_ATTR_TRANSPORT', '$tam_transport_1', 'SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE', '1']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_tam_collector_attr_src_ip_set")
    def test_sai_tam_collector_attr_src_ip_set(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "set",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_SRC_IP", 'TODO']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_tam_collector_attr_src_ip_set"])
    def test_sai_tam_collector_attr_src_ip_get(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "get",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_SRC_IP"]
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


    @pytest.mark.dependency(name="test_sai_tam_collector_attr_dst_ip_set")
    def test_sai_tam_collector_attr_dst_ip_set(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "set",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_DST_IP", 'TODO']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_tam_collector_attr_dst_ip_set"])
    def test_sai_tam_collector_attr_dst_ip_get(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "get",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_DST_IP"]
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


    @pytest.mark.dependency(name="test_sai_tam_collector_attr_localhost_set")
    def test_sai_tam_collector_attr_localhost_set(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "set",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_LOCALHOST", 'true']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_tam_collector_attr_localhost_set"])
    def test_sai_tam_collector_attr_localhost_get(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "get",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_LOCALHOST"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'true', 'Get error, expected true but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_tam_collector_attr_virtual_router_id_set")
    def test_sai_tam_collector_attr_virtual_router_id_set(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "set",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_VIRTUAL_ROUTER_ID", 'SAI_NULL_OBJECT_ID']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_tam_collector_attr_virtual_router_id_set"])
    def test_sai_tam_collector_attr_virtual_router_id_get(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "get",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_VIRTUAL_ROUTER_ID"]
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


    @pytest.mark.dependency(name="test_sai_tam_collector_attr_truncate_size_set")
    def test_sai_tam_collector_attr_truncate_size_set(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "set",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_TRUNCATE_SIZE", '0']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_tam_collector_attr_truncate_size_set"])
    def test_sai_tam_collector_attr_truncate_size_get(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "get",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_TRUNCATE_SIZE"]
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


    @pytest.mark.dependency(name="test_sai_tam_collector_attr_transport_set")
    def test_sai_tam_collector_attr_transport_set(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "set",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_TRANSPORT", 'TODO']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_tam_collector_attr_transport_set"])
    def test_sai_tam_collector_attr_transport_get(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "get",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_TRANSPORT"]
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


    @pytest.mark.dependency(name="test_sai_tam_collector_attr_dscp_value_set")
    def test_sai_tam_collector_attr_dscp_value_set(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "set",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE", 'TODO']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_tam_collector_attr_dscp_value_set"])
    def test_sai_tam_collector_attr_dscp_value_get(self, npu):

        commands = [
            {
                "name": "tam_collector_1",
                "op": "get",
                "attributes": ["SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE"]
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


    def test_tam_collector_remove(self, npu):

        commands = [{'name': 'tam_collector_1', 'op': 'remove'}, {'name': 'tam_transport_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

