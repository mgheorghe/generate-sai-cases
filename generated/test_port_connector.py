

from pprint import pprint

import pytest


class TestSaiPortConnector:

    @pytest.mark.dependency(scope='session')
    def test_port_connector_create(self, npu):

        commands = [{'name': 'port_connector_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR', 'attributes': ['SAI_PORT_CONNECTOR_ATTR_SYSTEM_SIDE_PORT_ID', 'sai_object_id_t', 'SAI_PORT_CONNECTOR_ATTR_LINE_SIDE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_port_connector_remove(self, npu):

        commands = [{'name': 'port_connector_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_PORT_CONNECTOR', 'attributes': ['SAI_PORT_CONNECTOR_ATTR_SYSTEM_SIDE_PORT_ID', 'sai_object_id_t', 'SAI_PORT_CONNECTOR_ATTR_LINE_SIDE_PORT_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

