from pprint import pprint

import pytest


class TestSaiQueue:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SCHEDULER_GROUP SAI_OBJECT_TYPE_PORT

    @pytest.mark.dependency(scope="session")
    def test_queue_create(self, npu):
        commands = [
            {
                "name": "queue_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_QUEUE",
                "attributes": [
                    "SAI_QUEUE_ATTR_TYPE",
                    "sai_queue_type_t",
                    "SAI_QUEUE_ATTR_PORT",
                    "sai_object_id_t",
                    "SAI_QUEUE_ATTR_INDEX",
                    "sai_uint8_t",
                    "SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE",
                    "sai_object_id_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_queue_remove(self, npu):
        commands = [
            {
                "name": "queue_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_QUEUE",
                "attributes": [
                    "SAI_QUEUE_ATTR_TYPE",
                    "sai_queue_type_t",
                    "SAI_QUEUE_ATTR_PORT",
                    "sai_object_id_t",
                    "SAI_QUEUE_ATTR_INDEX",
                    "sai_uint8_t",
                    "SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE",
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
