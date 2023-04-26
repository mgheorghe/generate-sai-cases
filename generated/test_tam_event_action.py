

from pprint import pprint

import pytest


class TestSaiTamEventAction:

    @pytest.mark.dependency(scope='session')
    def test_tam_event_action_create(self, npu):

        commands = [{'name': 'tam_event_action_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION', 'attributes': ['SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_event_action_remove(self, npu):

        commands = [{'name': 'tam_event_action_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION', 'attributes': ['SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

