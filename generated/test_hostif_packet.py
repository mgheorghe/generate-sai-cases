

from pprint import pprint

import pytest


class TestSaiHostifPacket:

    @pytest.mark.dependency(scope='session')
    def test_hostif_packet_create(self, npu):

        commands = [{'name': 'hostif_packet_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HOSTIF_PACKET', 'attributes': ['SAI_HOSTIF_PACKET_ATTR_HOSTIF_TX_TYPE', 'sai_hostif_tx_type_t', 'SAI_HOSTIF_PACKET_ATTR_EGRESS_PORT_OR_LAG', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_hostif_packet_remove(self, npu):

        commands = [{'name': 'hostif_packet_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HOSTIF_PACKET', 'attributes': ['SAI_HOSTIF_PACKET_ATTR_HOSTIF_TX_TYPE', 'sai_hostif_tx_type_t', 'SAI_HOSTIF_PACKET_ATTR_EGRESS_PORT_OR_LAG', 'sai_object_id_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

