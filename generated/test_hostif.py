from pprint import pprint

import pytest


class TestSaiHostif:
    # object with parent SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_VLAN SAI_OBJECT_TYPE_SYSTEM_PORT

    def test_hostif_create(self, npu):
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
                'name': 'hostif_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOSTIF',
                'attributes': [
                    'SAI_HOSTIF_ATTR_TYPE',
                    'SAI_HOSTIF_TYPE_NETDEV',
                    'SAI_HOSTIF_ATTR_OBJ_ID',
                    '$port_1',
                    'SAI_HOSTIF_ATTR_NAME',
                    'char',
                    'SAI_HOSTIF_ATTR_GENETLINK_MCGRP_NAME',
                    'char',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_hostif_attr_oper_status_set')
    def test_sai_hostif_attr_oper_status_set(self, npu):
        commands = [
            {
                'name': 'hostif_1',
                'op': 'set',
                'attributes': ['SAI_HOSTIF_ATTR_OPER_STATUS', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_attr_oper_status_set'])
    def test_sai_hostif_attr_oper_status_get(self, npu):
        commands = [
            {
                'name': 'hostif_1',
                'op': 'get',
                'attributes': ['SAI_HOSTIF_ATTR_OPER_STATUS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'false', (
            'Get error, expected false but got %s' % results[0][0].value()
        )

    @pytest.mark.dependency(name='test_sai_hostif_attr_queue_set')
    def test_sai_hostif_attr_queue_set(self, npu):
        commands = [
            {
                'name': 'hostif_1',
                'op': 'set',
                'attributes': ['SAI_HOSTIF_ATTR_QUEUE', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_attr_queue_set'])
    def test_sai_hostif_attr_queue_get(self, npu):
        commands = [
            {'name': 'hostif_1', 'op': 'get', 'attributes': ['SAI_HOSTIF_ATTR_QUEUE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[0][0].value()
        )

    @pytest.mark.dependency(name='test_sai_hostif_attr_vlan_tag_set')
    def test_sai_hostif_attr_vlan_tag_set(self, npu):
        commands = [
            {
                'name': 'hostif_1',
                'op': 'set',
                'attributes': ['SAI_HOSTIF_ATTR_VLAN_TAG', 'SAI_HOSTIF_VLAN_TAG_STRIP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_hostif_attr_vlan_tag_set'])
    def test_sai_hostif_attr_vlan_tag_get(self, npu):
        commands = [
            {
                'name': 'hostif_1',
                'op': 'get',
                'attributes': ['SAI_HOSTIF_ATTR_VLAN_TAG'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[0][0].value() == 'SAI_HOSTIF_VLAN_TAG_STRIP', (
            'Get error, expected SAI_HOSTIF_VLAN_TAG_STRIP but got %s'
            % results[0][0].value()
        )

    def test_hostif_remove(self, npu):
        commands = [
            {'name': 'hostif_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
