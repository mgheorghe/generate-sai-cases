

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_PORT
class TestSaiPortConnector:

    @pytest.mark.dependency(scope='session')
    def test_port_connector_create(self, npu):

        commands = [{'name': 'port_connector_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR', 'attributes': ['SAI_PORT_CONNECTOR_ATTR_SYSTEM_SIDE_PORT_ID', 'sai_object_id_t', 'SAI_PORT_CONNECTOR_ATTR_LINE_SIDE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_port_connector_remove(self, npu):

        commands = [{'name': 'port_connector_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR', 'attributes': ['SAI_PORT_CONNECTOR_ATTR_SYSTEM_SIDE_PORT_ID', 'sai_object_id_t', 'SAI_PORT_CONNECTOR_ATTR_LINE_SIDE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

