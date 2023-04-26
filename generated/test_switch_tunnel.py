

from pprint import pprint

import pytest


class TestSaiSwitchTunnel:

    @pytest.mark.dependency(scope='session')
    def test_switch_tunnel_create(self, npu):

        commands = [{'name': 'switch_tunnel_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL', 'attributes': ['SAI_SWITCH_TUNNEL_ATTR_TUNNEL_TYPE', 'sai_tunnel_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_switch_tunnel_remove(self, npu):

        commands = [{'name': 'switch_tunnel_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_SWITCH_TUNNEL', 'attributes': ['SAI_SWITCH_TUNNEL_ATTR_TUNNEL_TYPE', 'sai_tunnel_type_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

