from pprint import pprint

import pytest


class TestSaiTamCollector:
    # object with parent SAI_OBJECT_TYPE_TAM_TRANSPORT

    @pytest.mark.dependency(scope="session")
    def test_tam_collector_create(self, npu):
        commands = [
            {
                "name": "tam_collector_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_TAM_COLLECTOR",
                "attributes": [
                    "SAI_TAM_COLLECTOR_ATTR_SRC_IP",
                    "sai_ip_address_t",
                    "SAI_TAM_COLLECTOR_ATTR_DST_IP",
                    "sai_ip_address_t",
                    "SAI_TAM_COLLECTOR_ATTR_TRANSPORT",
                    "sai_object_id_t",
                    "SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE",
                    "sai_uint8_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_tam_collector_remove(self, npu):
        commands = [
            {
                "name": "tam_collector_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_TAM_COLLECTOR",
                "attributes": [
                    "SAI_TAM_COLLECTOR_ATTR_SRC_IP",
                    "sai_ip_address_t",
                    "SAI_TAM_COLLECTOR_ATTR_DST_IP",
                    "sai_ip_address_t",
                    "SAI_TAM_COLLECTOR_ATTR_TRANSPORT",
                    "sai_object_id_t",
                    "SAI_TAM_COLLECTOR_ATTR_DSCP_VALUE",
                    "sai_uint8_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == "SAI_STATUS_SUCCESS" for result in results]
        ), "Remove error"
