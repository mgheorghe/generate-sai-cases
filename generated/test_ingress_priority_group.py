

from pprint import pprint

import pytest


class TestSaiIngressPriorityGroup:

    @pytest.mark.dependency(scope='session')
    def test_ingress_priority_group_create(self, npu):

        commands = [{'name': 'ingress_priority_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP', 'attributes': ['SAI_INGRESS_PRIORITY_GROUP_ATTR_PORT', 'sai_object_id_t', 'SAI_INGRESS_PRIORITY_GROUP_ATTR_INDEX', 'sai_uint8_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_ingress_priority_group_remove(self, npu):

        commands = [{'name': 'ingress_priority_group_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP', 'attributes': ['SAI_INGRESS_PRIORITY_GROUP_ATTR_PORT', 'sai_object_id_t', 'SAI_INGRESS_PRIORITY_GROUP_ATTR_INDEX', 'sai_uint8_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

