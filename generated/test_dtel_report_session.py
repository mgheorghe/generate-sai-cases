

from pprint import pprint

import pytest


class TestSaiDtelReportSession:

    @pytest.mark.dependency(scope='session')
    def test_dtel_report_session_create(self, npu):

        commands = [{'name': 'dtel_report_session_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_dtel_report_session_remove(self, npu):

        commands = [{'name': 'dtel_report_session_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_DTEL_REPORT_SESSION', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
