from pprint import pprint

import pytest


class TestSaiMacsecSc:
    # object with parent SAI_OBJECT_TYPE_MACSEC_FLOW

    def test_macsec_sc_create(self, npu):
        commands = [
            {
                'name': 'macsec_flow_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW',
                'attributes': [
                    'SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                ],
            },
            {
                'name': 'macsec_sc_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'attributes': [
                    'SAI_MACSEC_SC_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_SC_ATTR_FLOW_ID',
                    '$macsec_flow_1',
                    'SAI_MACSEC_SC_ATTR_MACSEC_SCI',
                    '10',
                    'SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE',
                    'SAI_MACSEC_CIPHER_SUITE_GCM_AES_128',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_macsec_sc_attr_macsec_explicit_sci_enable_set(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_MACSEC_EXPLICIT_SCI_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_macsec_sc_attr_macsec_explicit_sci_enable_set']
    )
    def test_sai_macsec_sc_attr_macsec_explicit_sci_enable_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_EXPLICIT_SCI_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_macsec_sc_attr_macsec_sectag_offset_set(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_MACSEC_SECTAG_OFFSET', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_macsec_sc_attr_macsec_sectag_offset_set']
    )
    def test_sai_macsec_sc_attr_macsec_sectag_offset_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_SECTAG_OFFSET',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    def test_sai_macsec_sc_attr_active_egress_sa_id_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_ACTIVE_EGRESS_SA_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_macsec_sc_attr_macsec_replay_protection_enable_set(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': [
                    'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_ENABLE',
                    'true',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_macsec_sc_attr_macsec_replay_protection_enable_set']
    )
    def test_sai_macsec_sc_attr_macsec_replay_protection_enable_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'true', (
            'Get error, expected true but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_macsec_sc_attr_macsec_replay_protection_window_set(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': [
                    'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_WINDOW',
                    '0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_macsec_sc_attr_macsec_replay_protection_window_set']
    )
    def test_sai_macsec_sc_attr_macsec_replay_protection_window_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_WINDOW',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    def test_sai_macsec_sc_attr_sa_list_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_SA_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_macsec_sc_attr_macsec_cipher_suite_set(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_macsec_sc_attr_macsec_cipher_suite_set'])
    def test_sai_macsec_sc_attr_macsec_cipher_suite_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_macsec_sc_attr_encryption_enable_set(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_ENCRYPTION_ENABLE', 'true'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_macsec_sc_attr_encryption_enable_set'])
    def test_sai_macsec_sc_attr_encryption_enable_get(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_ENCRYPTION_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'true', (
            'Get error, expected true but got %s' % results[1][0].value()
        )

    def test_macsec_sc_remove(self, npu):
        commands = [
            {
                'name': 'macsec_sc_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'attributes': [
                    'SAI_MACSEC_SC_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_SC_ATTR_FLOW_ID',
                    '$macsec_flow_1',
                    'SAI_MACSEC_SC_ATTR_MACSEC_SCI',
                    '10',
                    'SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE',
                    'SAI_MACSEC_CIPHER_SUITE_GCM_AES_128',
                ],
            },
            {
                'name': 'macsec_flow_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW',
                'attributes': [
                    'SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
