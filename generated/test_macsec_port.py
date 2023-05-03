from pprint import pprint

import pytest


class TestSaiMacsecPort:
    # object with parent SAI_OBJECT_TYPE_PORT

    def test_macsec_port_create(self, npu):
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
                'name': 'macsec_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'attributes': [
                    'SAI_MACSEC_PORT_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_PORT_ATTR_PORT_ID',
                    '$port_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_macsec_port_attr_ctag_enable_set(self, npu):
        commands = [
            {
                'name': 'macsec_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'atrribute': ['SAI_MACSEC_PORT_ATTR_CTAG_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_macsec_port_attr_ctag_enable_set'])
    def test_sai_macsec_port_attr_ctag_enable_get(self, npu):
        commands = [
            {
                'name': 'macsec_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'atrribute': 'SAI_MACSEC_PORT_ATTR_CTAG_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_macsec_port_attr_stag_enable_set(self, npu):
        commands = [
            {
                'name': 'macsec_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'atrribute': ['SAI_MACSEC_PORT_ATTR_STAG_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_macsec_port_attr_stag_enable_set'])
    def test_sai_macsec_port_attr_stag_enable_get(self, npu):
        commands = [
            {
                'name': 'macsec_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'atrribute': 'SAI_MACSEC_PORT_ATTR_STAG_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_macsec_port_attr_switch_switching_mode_set(self, npu):
        commands = [
            {
                'name': 'macsec_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'atrribute': [
                    'SAI_MACSEC_PORT_ATTR_SWITCH_SWITCHING_MODE',
                    'SAI_SWITCH_SWITCHING_MODE_CUT_THROUGH',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_macsec_port_attr_switch_switching_mode_set']
    )
    def test_sai_macsec_port_attr_switch_switching_mode_get(self, npu):
        commands = [
            {
                'name': 'macsec_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'atrribute': 'SAI_MACSEC_PORT_ATTR_SWITCH_SWITCHING_MODE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'SAI_SWITCH_SWITCHING_MODE_CUT_THROUGH', (
            'Get error, expected SAI_SWITCH_SWITCHING_MODE_CUT_THROUGH but got %s'
            % results[1][0].value()
        )

    def test_macsec_port_remove(self, npu):
        commands = [
            {
                'name': 'macsec_port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'attributes': [
                    'SAI_MACSEC_PORT_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_PORT_ATTR_PORT_ID',
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
