from pprint import pprint

import pytest


class TestSaiIsolationGroupMember:
    # object with parent SAI_OBJECT_TYPE_ISOLATION_GROUP SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_BRIDGE_PORT

    @pytest.mark.dependency(scope="session")
    def test_isolation_group_member_create(self, npu):
        commands = [
            {
                "name": "isolation_group_member_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_ISOLATION_GROUP_MEMBER",
                "attributes": [
                    "SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_GROUP_ID",
                    "sai_object_id_t",
                    "SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_OBJECT",
                    "sai_object_id_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_isolation_group_member_remove(self, npu):
        commands = [
            {
                "name": "isolation_group_member_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_ISOLATION_GROUP_MEMBER",
                "attributes": [
                    "SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_GROUP_ID",
                    "sai_object_id_t",
                    "SAI_ISOLATION_GROUP_MEMBER_ATTR_ISOLATION_OBJECT",
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
