

from pprint import pprint

import pytest


class TestSaiDebugCounter:

    @pytest.mark.dependency(scope='session')
    def test_debug_counter_create(self, npu):

        commands = [{'name': 'debug_counter_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER', 'attributes': ['SAI_DEBUG_COUNTER_ATTR_TYPE', 'sai_debug_counter_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_debug_counter_remove(self, npu):

        commands = [{'name': 'debug_counter_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER', 'attributes': ['SAI_DEBUG_COUNTER_ATTR_TYPE', 'sai_debug_counter_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
