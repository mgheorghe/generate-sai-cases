
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiNatZoneCounter:
    # object with no attributes

    def test_nat_zone_counter_create(self, npu):

        commands = [{'name': 'nat_zone_counter_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    @pytest.mark.dependency(name="test_sai_nat_zone_counter_attr_nat_type_set")
    def test_sai_nat_zone_counter_attr_nat_type_set(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "set",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_NAT_TYPE", 'SAI_NAT_TYPE_NONE']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_nat_zone_counter_attr_nat_type_set"])
    def test_sai_nat_zone_counter_attr_nat_type_get(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "get",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_NAT_TYPE"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_NAT_TYPE_NONE', 'Get error, expected SAI_NAT_TYPE_NONE but got %s' %  r_value


    @pytest.mark.dependency(name="test_sai_nat_zone_counter_attr_zone_id_set")
    def test_sai_nat_zone_counter_attr_zone_id_set(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "set",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_ZONE_ID", '0']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_nat_zone_counter_attr_zone_id_set"])
    def test_sai_nat_zone_counter_attr_zone_id_get(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "get",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_ZONE_ID"]
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


    @pytest.mark.dependency(name="test_sai_nat_zone_counter_attr_discard_packet_count_set")
    def test_sai_nat_zone_counter_attr_discard_packet_count_set(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "set",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_DISCARD_PACKET_COUNT", '0']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_nat_zone_counter_attr_discard_packet_count_set"])
    def test_sai_nat_zone_counter_attr_discard_packet_count_get(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "get",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_DISCARD_PACKET_COUNT"]
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


    @pytest.mark.dependency(name="test_sai_nat_zone_counter_attr_translation_needed_packet_count_set")
    def test_sai_nat_zone_counter_attr_translation_needed_packet_count_set(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "set",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATION_NEEDED_PACKET_COUNT", '0']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_nat_zone_counter_attr_translation_needed_packet_count_set"])
    def test_sai_nat_zone_counter_attr_translation_needed_packet_count_get(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "get",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATION_NEEDED_PACKET_COUNT"]
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


    @pytest.mark.dependency(name="test_sai_nat_zone_counter_attr_translations_packet_count_set")
    def test_sai_nat_zone_counter_attr_translations_packet_count_set(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "set",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATIONS_PACKET_COUNT", '0']
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        pprint(results)



    @pytest.mark.dependency(depends=["test_sai_nat_zone_counter_attr_translations_packet_count_set"])
    def test_sai_nat_zone_counter_attr_translations_packet_count_get(self, npu):

        commands = [
            {
                "name": "nat_zone_counter_1",
                "op": "get",
                "attributes": ["SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATIONS_PACKET_COUNT"]
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


    def test_nat_zone_counter_remove(self, npu):

        commands = [{'name': 'nat_zone_counter_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

