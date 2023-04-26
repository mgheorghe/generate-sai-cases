

from pprint import pprint

import pytest

# object with no attributes
class TestSaiDtelQueueReport:

    @pytest.mark.dependency(scope='session')
    def test_dtel_queue_report_create(self, npu):

        commands = [{'name': 'dtel_queue_report_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DTEL_QUEUE_REPORT', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_dtel_queue_report_remove(self, npu):

        commands = [{'name': 'dtel_queue_report_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DTEL_QUEUE_REPORT', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

