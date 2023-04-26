

from pprint import pprint

import pytest


class TestSaiTamInt:

    @pytest.mark.dependency(scope='session')
    def test_tam_int_create(self, npu):

        commands = [{'name': 'tam_int_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_INT', 'attributes': ['SAI_TAM_INT_ATTR_TYPE', 'sai_tam_int_type_t', 'SAI_TAM_INT_ATTR_DEVICE_ID', 'sai_uint32_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_TYPE', 'sai_tam_int_presence_type_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_PB1', 'sai_uint32_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_PB2', 'sai_uint32_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_DSCP_VALUE', 'sai_uint8_t', 'SAI_TAM_INT_ATTR_INLINE', 'bool', 'SAI_TAM_INT_ATTR_INT_PRESENCE_L3_PROTOCOL', 'sai_uint8_t', 'SAI_TAM_INT_ATTR_REPORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_int_remove(self, npu):

        commands = [{'name': 'tam_int_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_INT', 'attributes': ['SAI_TAM_INT_ATTR_TYPE', 'sai_tam_int_type_t', 'SAI_TAM_INT_ATTR_DEVICE_ID', 'sai_uint32_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_TYPE', 'sai_tam_int_presence_type_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_PB1', 'sai_uint32_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_PB2', 'sai_uint32_t', 'SAI_TAM_INT_ATTR_INT_PRESENCE_DSCP_VALUE', 'sai_uint8_t', 'SAI_TAM_INT_ATTR_INLINE', 'bool', 'SAI_TAM_INT_ATTR_INT_PRESENCE_L3_PROTOCOL', 'sai_uint8_t', 'SAI_TAM_INT_ATTR_REPORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

