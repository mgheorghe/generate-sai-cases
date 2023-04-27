from pprint import pprint

import pytest


class TestSaiRpfGroupMember:
    # object with parent SAI_OBJECT_TYPE_RPF_GROUP SAI_OBJECT_TYPE_ROUTER_INTERFACE

    @pytest.mark.dependency(scope="session")
    def test_rpf_group_member_create(self, npu):
        commands = [
            {
                "name": "rpf_group_member_1",
                "op": "create",
                "type": "SAI_OBJECT_TYPE_RPF_GROUP_MEMBER",
                "attributes": [
                    "SAI_RPF_GROUP_MEMBER_ATTR_RPF_GROUP_ID",
                    "sai_object_id_t",
                    "SAI_RPF_GROUP_MEMBER_ATTR_RPF_INTERFACE_ID",
                    "sai_object_id_t",
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_rpf_group_member_remove(self, npu):
        commands = [
            {
                "name": "rpf_group_member_1",
                "op": "remove",
                "type": "SAI_OBJECT_TYPE_RPF_GROUP_MEMBER",
                "attributes": [
                    "SAI_RPF_GROUP_MEMBER_ATTR_RPF_GROUP_ID",
                    "sai_object_id_t",
                    "SAI_RPF_GROUP_MEMBER_ATTR_RPF_INTERFACE_ID",
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
