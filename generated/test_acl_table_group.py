from pprint import pprint

import pytest


class TestSaiAclTableGroup:
    # object with no parents

    @pytest.mark.dependency(scope="session")
    def test_acl_table_group_create(self, npu):
        commands = [
            {
                "name": "acl_table_group_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_ACL_TABLE_GROUP",
                "attributes": ["SAI_ACL_TABLE_GROUP_ATTR_ACL_STAGE", "sai_acl_stage_t"],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_acl_table_group_remove(self, npu):
        commands = [
            {
                "name": "acl_table_group_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_ACL_TABLE_GROUP",
                "attributes": ["SAI_ACL_TABLE_GROUP_ATTR_ACL_STAGE", "sai_acl_stage_t"],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all(
            [result == "SAI_STATUS_SUCCESS" for result in results]
        ), "Remove error"
