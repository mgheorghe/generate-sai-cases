from pprint import pprint

import pytest


@pytest.mark.dpu
class TestSaiEniEtherAddressMapEntry:
    # object with no attributes

    def test_eni_ether_address_map_entry_create(self, dpu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'address': 'TODO'},
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_eni_ether_address_map_entry_attr_eni_id_set')
    def test_sai_eni_ether_address_map_entry_attr_eni_id_set(self, dpu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'set',
                'attributes': ['SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID', 'null'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_eni_ether_address_map_entry_attr_eni_id_set']
    )
    def test_sai_eni_ether_address_map_entry_attr_eni_id_get(self, dpu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'get',
                'attributes': ['SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    def test_eni_ether_address_map_entry_remove(self, dpu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'key': {'switch_id': '$SWITCH_ID', 'address': 'TODO'},
                'op': 'remove',
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
