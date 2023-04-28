from pprint import pprint

import pytest


class TestSaiHostifPacket:
    # object with parent SAI_OBJECT_TYPE_PORT

    @pytest.mark.dependency(scope='session')
    def test_hostif_packet_create(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'hostif_packet_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_PACKET',
                'attributes': [
                    'SAI_HOSTIF_PACKET_ATTR_HOSTIF_TX_TYPE',
                    'SAI_HOSTIF_TX_TYPE_PIPELINE_BYPASS',
                    'SAI_HOSTIF_PACKET_ATTR_EGRESS_PORT_OR_LAG',
                    '$port_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_hostif_packet_remove(self, npu):
        commands = [
            {
                'name': 'hostif_packet_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_HOSTIF_PACKET',
                'attributes': [
                    'SAI_HOSTIF_PACKET_ATTR_HOSTIF_TX_TYPE',
                    'SAI_HOSTIF_TX_TYPE_PIPELINE_BYPASS',
                    'SAI_HOSTIF_PACKET_ATTR_EGRESS_PORT_OR_LAG',
                    '$port_1',
                ],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
