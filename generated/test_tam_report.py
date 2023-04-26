

from pprint import pprint

import pytest


class TestSaiTamReport:

    @pytest.mark.dependency(scope='session')
    def test_tam_report_create(self, npu):

        commands = [{'name': 'tam_report_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_REPORT', 'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'sai_tam_report_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_report_remove(self, npu):

        commands = [{'name': 'tam_report_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_REPORT', 'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'sai_tam_report_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

