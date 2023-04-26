

from pprint import pprint

import pytest


class TestSaiTunnel:

    @pytest.mark.dependency(scope='session')
    def test_tunnel_create(self, npu):

        commands = [{'name': 'tunnel_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TUNNEL', 'attributes': ['SAI_TUNNEL_ATTR_TYPE', 'sai_tunnel_type_t', 'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE', 'sai_object_id_t', 'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tunnel_remove(self, npu):

        commands = [{'name': 'tunnel_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TUNNEL', 'attributes': ['SAI_TUNNEL_ATTR_TYPE', 'sai_tunnel_type_t', 'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE', 'sai_object_id_t', 'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

