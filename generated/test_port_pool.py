

from pprint import pprint

import pytest


class TestSaiPortPool:

    @pytest.mark.dependency(scope='session')
    def test_port_pool_create(self, npu):

        commands = [{'name': 'port_pool_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_PORT_POOL', 'attributes': ['SAI_PORT_POOL_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_PORT_POOL_ATTR_BUFFER_POOL_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_port_pool_remove(self, npu):

        commands = [{'name': 'port_pool_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_PORT_POOL', 'attributes': ['SAI_PORT_POOL_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_PORT_POOL_ATTR_BUFFER_POOL_ID', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

