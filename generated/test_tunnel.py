

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_ROUTER_INTERFACE SAI_OBJECT_TYPE_ROUTER_INTERFACE
class TestSaiTunnel:

    @pytest.mark.dependency(scope='session')
    def test_tunnel_create(self, npu):

        commands = [{'name': 'tunnel_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TUNNEL', 'attributes': ['SAI_TUNNEL_ATTR_TYPE', 'SAI_TUNNEL_TYPE_IPINIP', 'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE', 'sai_object_id_t', 'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_tunnel_remove(self, npu):

        commands = [{'name': 'tunnel_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TUNNEL', 'attributes': ['SAI_TUNNEL_ATTR_TYPE', 'SAI_TUNNEL_TYPE_IPINIP', 'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE', 'sai_object_id_t', 'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
