

from pprint import pprint

import pytest


class TestSaiTamTelType:

    @pytest.mark.dependency(scope='session')
    def test_tam_tel_type_create(self, npu):

        commands = [{'name': 'tam_tel_type_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE', 'attributes': ['SAI_TAM_TEL_TYPE_ATTR_TAM_TELEMETRY_TYPE', 'sai_tam_telemetry_type_t', 'SAI_TAM_TEL_TYPE_ATTR_REPORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_tel_type_remove(self, npu):

        commands = [{'name': 'tam_tel_type_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_TEL_TYPE', 'attributes': ['SAI_TAM_TEL_TYPE_ATTR_TAM_TELEMETRY_TYPE', 'sai_tam_telemetry_type_t', 'SAI_TAM_TEL_TYPE_ATTR_REPORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

