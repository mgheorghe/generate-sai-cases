from pprint import pprint

import pytest


class TestSaiEniEtherAddressMapEntry:
    # object with no attributes

    def test_eni_ether_address_map_entry_create(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'address': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_eni_ether_address_map_entry_attr_eni_id_set(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'atrribute': [
                    'SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_eni_ether_address_map_entry_attr_eni_id_set']
    )
    def test_sai_eni_ether_address_map_entry_attr_eni_id_get(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'atrribute': 'SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_NULL_OBJECT_ID', (
            'Get error, expected SAI_NULL_OBJECT_ID but got %s' % results[1][0].value()
        )

    def test_eni_ether_address_map_entry_remove(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'address': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
