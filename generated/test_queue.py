

from pprint import pprint

import pytest


class TestSaiQueue:

    @pytest.mark.dependency(scope='session')
    def test_queue_create(self, npu):

        commands = [{'name': 'queue_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_QUEUE', 'attributes': ['SAI_QUEUE_ATTR_TYPE', 'sai_queue_type_t', 'SAI_QUEUE_ATTR_PORT', 'sai_object_id_t', 'SAI_QUEUE_ATTR_INDEX', 'sai_uint8_t', 'SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_queue_remove(self, npu):

        commands = [{'name': 'queue_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_QUEUE', 'attributes': ['SAI_QUEUE_ATTR_TYPE', 'sai_queue_type_t', 'SAI_QUEUE_ATTR_PORT', 'sai_object_id_t', 'SAI_QUEUE_ATTR_INDEX', 'sai_uint8_t', 'SAI_QUEUE_ATTR_PARENT_SCHEDULER_NODE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

