

from pprint import pprint

import pytest


class TestSaiDtelEvent:

    @pytest.mark.dependency(scope='session')
    def test_dtel_event_create(self, npu):

        commands = [{'name': 'dtel_event_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DTEL_EVENT', 'attributes': ['SAI_DTEL_EVENT_ATTR_TYPE', 'sai_dtel_event_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_dtel_event_remove(self, npu):

        commands = [{'name': 'dtel_event_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DTEL_EVENT', 'attributes': ['SAI_DTEL_EVENT_ATTR_TYPE', 'sai_dtel_event_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

