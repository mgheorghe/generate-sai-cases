from pprint import pprint

import pytest


class TestSaiStpPort:
    # object with parent SAI_OBJECT_TYPE_STP SAI_OBJECT_TYPE_BRIDGE_PORT

    @pytest.mark.dependency(scope="session")
    def test_stp_port_create(self, npu):
        commands = [
            {
                "name": "stp_port_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_STP_PORT",
                "attributes": [
                    "SAI_STP_PORT_ATTR_STP",
                    "sai_object_id_t",
                    "SAI_STP_PORT_ATTR_BRIDGE_PORT",
                    "sai_object_id_t",
                    "SAI_STP_PORT_ATTR_STATE",
                    "sai_stp_port_state_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_stp_port_remove(self, npu):
        commands = [
            {
                "name": "stp_port_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_STP_PORT",
                "attributes": [
                    "SAI_STP_PORT_ATTR_STP",
                    "sai_object_id_t",
                    "SAI_STP_PORT_ATTR_BRIDGE_PORT",
                    "sai_object_id_t",
                    "SAI_STP_PORT_ATTR_STATE",
                    "sai_stp_port_state_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == "SAI_STATUS_SUCCESS" for result in results]
        ), "Remove error"
