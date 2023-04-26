

from pprint import pprint

import pytest


class TestSaiTamEventThreshold:

    @pytest.mark.dependency(scope='session')
    def test_tam_event_threshold_create(self, npu):

        commands = [{'name': 'tam_event_threshold_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_event_threshold_remove(self, npu):

        commands = [{'name': 'tam_event_threshold_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_EVENT_THRESHOLD', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

