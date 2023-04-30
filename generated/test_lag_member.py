from pprint import pprint

import pytest


class TestSaiLagMember:
    # object with parent SAI_OBJECT_TYPE_LAG SAI_OBJECT_TYPE_PORT SAI_OBJECT_TYPE_SYSTEM_PORT

    def test_lag_member_create(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'attributes': [],
            },
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
                'name': 'lag_member_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_LAG_MEMBER',
                'attributes': [
                    'SAI_LAG_MEMBER_ATTR_LAG_ID',
                    '$lag_1',
                    'SAI_LAG_MEMBER_ATTR_PORT_ID',
                    '$port_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_lag_member_attr_egress_disable_set(self, npu):
        commands = [
            {
                'name': 'sai_lag_member_attr_egress_disable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG_MEMBER',
                'atrribute': ['SAI_LAG_MEMBER_ATTR_EGRESS_DISABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_member_attr_egress_disable_get(self, npu):
        commands = [
            {
                'name': 'sai_lag_member_attr_egress_disable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG_MEMBER',
                'atrribute': 'SAI_LAG_MEMBER_ATTR_EGRESS_DISABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_lag_member_attr_ingress_disable_set(self, npu):
        commands = [
            {
                'name': 'sai_lag_member_attr_ingress_disable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG_MEMBER',
                'atrribute': ['SAI_LAG_MEMBER_ATTR_INGRESS_DISABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_lag_member_attr_ingress_disable_get(self, npu):
        commands = [
            {
                'name': 'sai_lag_member_attr_ingress_disable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_LAG_MEMBER',
                'atrribute': 'SAI_LAG_MEMBER_ATTR_INGRESS_DISABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_lag_member_remove(self, npu):
        commands = [
            {
                'name': 'lag_member_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_LAG_MEMBER',
                'attributes': [
                    'SAI_LAG_MEMBER_ATTR_LAG_ID',
                    '$lag_1',
                    'SAI_LAG_MEMBER_ATTR_PORT_ID',
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
            {
                'name': 'lag_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
