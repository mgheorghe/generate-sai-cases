

from pprint import pprint

import pytest


class TestSaiSystemPort:

    @pytest.mark.dependency(scope='session')
    def test_system_port_create(self, npu):

        commands = [{'name': 'system_port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT', 'attributes': ['SAI_SYSTEM_PORT_ATTR_CONFIG_INFO', 'sai_system_port_config_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_system_port_remove(self, npu):

        commands = [{'name': 'system_port_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT', 'attributes': ['SAI_SYSTEM_PORT_ATTR_CONFIG_INFO', 'sai_system_port_config_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

