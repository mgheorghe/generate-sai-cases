

from pprint import pprint

import pytest


class TestSaiIpsecPort:

    @pytest.mark.dependency(scope='session')
    def test_ipsec_port_create(self, npu):

        commands = [{'name': 'ipsec_port_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_IPSEC_PORT', 'attributes': ['SAI_IPSEC_PORT_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_IPSEC_PORT_ATTR_NATIVE_VLAN_ID', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_ipsec_port_remove(self, npu):

        commands = [{'name': 'ipsec_port_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_IPSEC_PORT', 'attributes': ['SAI_IPSEC_PORT_ATTR_PORT_ID', 'sai_object_id_t', 'SAI_IPSEC_PORT_ATTR_NATIVE_VLAN_ID', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

