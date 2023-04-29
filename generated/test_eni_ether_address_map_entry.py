from pprint import pprint

import pytest


class TestSaiEniEtherAddressMapEntry:
    # object with no attributes

    @pytest.mark.dependency(scope='session')
    def test_eni_ether_address_map_entry_create(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_eni_ether_address_map_entry_attr_eni_id_set(self, dpu):
        commands = [
            {
                'name': 'sai_eni_ether_address_map_entry_attr_eni_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'atrribute': [
                    'SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_eni_ether_address_map_entry_attr_eni_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_eni_ether_address_map_entry_attr_eni_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'atrribute': 'SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_eni_ether_address_map_entry_remove(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
