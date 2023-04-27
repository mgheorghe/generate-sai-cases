from pprint import pprint

import pytest


class TestSaiBridgePort:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_SYSTEM_PORT SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_TUNNEL SAI_OBJECT_TYPE_BRIDGE

    @pytest.mark.dependency(scope="session")
    def test_bridge_port_create(self, npu):
        commands = [
            {
                "name": "bridge_port_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_BRIDGE_PORT",
                "attributes": [
                    "SAI_BRIDGE_PORT_ATTR_TYPE",
                    "sai_bridge_port_type_t",
                    "SAI_BRIDGE_PORT_ATTR_PORT_ID",
                    "sai_object_id_t",
                    "SAI_BRIDGE_PORT_ATTR_VLAN_ID",
                    "10",
                    "SAI_BRIDGE_PORT_ATTR_RIF_ID",
                    "sai_object_id_t",
                    "SAI_BRIDGE_PORT_ATTR_TUNNEL_ID",
                    "sai_object_id_t",
                    "SAI_BRIDGE_PORT_ATTR_BRIDGE_ID",
                    "sai_object_id_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_bridge_port_remove(self, npu):
        commands = [
            {
                "name": "bridge_port_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_BRIDGE_PORT",
                "attributes": [
                    "SAI_BRIDGE_PORT_ATTR_TYPE",
                    "sai_bridge_port_type_t",
                    "SAI_BRIDGE_PORT_ATTR_PORT_ID",
                    "sai_object_id_t",
                    "SAI_BRIDGE_PORT_ATTR_VLAN_ID",
                    "10",
                    "SAI_BRIDGE_PORT_ATTR_RIF_ID",
                    "sai_object_id_t",
                    "SAI_BRIDGE_PORT_ATTR_TUNNEL_ID",
                    "sai_object_id_t",
                    "SAI_BRIDGE_PORT_ATTR_BRIDGE_ID",
                    "sai_object_id_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == "SAI_STATUS_SUCCESS" for result in results]
        ), "Remove error"
