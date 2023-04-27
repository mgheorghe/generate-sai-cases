from pprint import pprint

import pytest


class TestSaiPort:
    # object with no parents

    @pytest.mark.dependency(scope="session")
    def test_port_create(self, npu):
        commands = [
            {
                "name": "port_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_PORT",
                "attributes": [
                    "SAI_PORT_ATTR_HW_LANE_LIST",
                    "sai_u32_list_t",
                    "SAI_PORT_ATTR_SPEED",
                    "sai_uint32_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_port_remove(self, npu):
        commands = [
            {
                "name": "port_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_PORT",
                "attributes": [
                    "SAI_PORT_ATTR_HW_LANE_LIST",
                    "sai_u32_list_t",
                    "SAI_PORT_ATTR_SPEED",
                    "sai_uint32_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == "SAI_STATUS_SUCCESS" for result in results]
        ), "Remove error"
