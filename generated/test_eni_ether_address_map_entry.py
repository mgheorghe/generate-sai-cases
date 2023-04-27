from pprint import pprint

import pytest


class TestSaiEniEtherAddressMapEntry:
    # object with no attributes

    @pytest.mark.dependency(scope="session")
    def test_eni_ether_address_map_entry_create(self, npu):
        commands = [
            {
                "name": "eni_ether_address_map_entry_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
                "attributes": [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_eni_ether_address_map_entry_remove(self, npu):
        commands = [
            {
                "name": "eni_ether_address_map_entry_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
                "attributes": [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == "SAI_STATUS_SUCCESS" for result in results]
        ), "Remove error"
