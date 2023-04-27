from pprint import pprint

import pytest


class TestSaiNextHop:
    # object with parent SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_TUNNEL SAI_OBJECT_TYPE_SRV6_SIDLIST

    @pytest.mark.dependency(scope="session")
    def test_next_hop_create(self, npu):
        commands = [
            {
                "name": "next_hop_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_NEXT_HOP",
                "attributes": [
                    "SAI_NEXT_HOP_ATTR_TYPE",
                    "sai_next_hop_type_t",
                    "SAI_NEXT_HOP_ATTR_IP",
                    "sai_ip_address_t",
                    "SAI_NEXT_HOP_ATTR_ROUTER_INTERFACE_ID",
                    "sai_object_id_t",
                    "SAI_NEXT_HOP_ATTR_TUNNEL_ID",
                    "sai_object_id_t",
                    "SAI_NEXT_HOP_ATTR_SRV6_SIDLIST_ID",
                    "sai_object_id_t",
                    "SAI_NEXT_HOP_ATTR_LABELSTACK",
                    "sai_u32_list_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_next_hop_remove(self, npu):
        commands = [
            {
                "name": "next_hop_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_NEXT_HOP",
                "attributes": [
                    "SAI_NEXT_HOP_ATTR_TYPE",
                    "sai_next_hop_type_t",
                    "SAI_NEXT_HOP_ATTR_IP",
                    "sai_ip_address_t",
                    "SAI_NEXT_HOP_ATTR_ROUTER_INTERFACE_ID",
                    "sai_object_id_t",
                    "SAI_NEXT_HOP_ATTR_TUNNEL_ID",
                    "sai_object_id_t",
                    "SAI_NEXT_HOP_ATTR_SRV6_SIDLIST_ID",
                    "sai_object_id_t",
                    "SAI_NEXT_HOP_ATTR_LABELSTACK",
                    "sai_u32_list_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == "SAI_STATUS_SUCCESS" for result in results]
        ), "Remove error"
