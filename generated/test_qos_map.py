

from pprint import pprint

import pytest

# object with no parents
class TestSaiQosMap:

    @pytest.mark.dependency(scope='session')
    def test_qos_map_create(self, npu):

        commands = [{'name': 'qos_map_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_QOS_MAP', 'attributes': ['SAI_QOS_MAP_ATTR_TYPE', 'sai_qos_map_type_t', 'SAI_QOS_MAP_ATTR_MAP_TO_VALUE_LIST', 'sai_qos_map_list_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_qos_map_remove(self, npu):

        commands = [{'name': 'qos_map_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_QOS_MAP', 'attributes': ['SAI_QOS_MAP_ATTR_TYPE', 'sai_qos_map_type_t', 'SAI_QOS_MAP_ATTR_MAP_TO_VALUE_LIST', 'sai_qos_map_list_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

