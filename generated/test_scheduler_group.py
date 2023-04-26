

from pprint import pprint

import pytest


class TestSaiSchedulerGroup:

    @pytest.mark.dependency(scope='session')
    def test_scheduler_group_create(self, npu):

        commands = [{'name': 'scheduler_group_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP', 'attributes': ['SAI_SCHEDULER_GROUP_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_SCHEDULER_GROUP_ATTR_LEVEL', 'sai_uint8_t', 'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS', 'sai_uint8_t', 'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_scheduler_group_remove(self, npu):

        commands = [{'name': 'scheduler_group_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_SCHEDULER_GROUP', 'attributes': ['SAI_SCHEDULER_GROUP_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_SCHEDULER_GROUP_ATTR_LEVEL', 'sai_uint8_t', 'SAI_SCHEDULER_GROUP_ATTR_MAX_CHILDS', 'sai_uint8_t', 'SAI_SCHEDULER_GROUP_ATTR_PARENT_NODE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

