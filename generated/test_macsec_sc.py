from pprint import pprint

import pytest


class TestSaiMacsecSc:
    # object with parent SAI_OBJECT_TYPE_MACSEC_FLOW

    @pytest.mark.dependency(scope='session')
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
                    'sai_macsec_cipher_suite_t',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_macsec_sc_attr_macsec_explicit_sci_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_explicit_sci_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_MACSEC_EXPLICIT_SCI_ENABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_explicit_sci_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_explicit_sci_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_EXPLICIT_SCI_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_sectag_offset_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_sectag_offset_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_MACSEC_SECTAG_OFFSET', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_sectag_offset_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_sectag_offset_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_SECTAG_OFFSET',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_active_egress_sa_id_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_active_egress_sa_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_ACTIVE_EGRESS_SA_ID',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_replay_protection_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_replay_protection_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': [
                    'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_ENABLE',
                    'true',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_replay_protection_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_replay_protection_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_replay_protection_window_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_replay_protection_window_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': [
                    'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_WINDOW',
                    '0',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_replay_protection_window_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_replay_protection_window_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_REPLAY_PROTECTION_WINDOW',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_sa_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_sa_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_SA_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_cipher_suite_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_cipher_suite_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_macsec_cipher_suite_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_macsec_cipher_suite_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_encryption_enable_set(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_encryption_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': ['SAI_MACSEC_SC_ATTR_ENCRYPTION_ENABLE', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_macsec_sc_attr_encryption_enable_get(self, dpu):
        commands = [
            {
                'name': 'sai_macsec_sc_attr_encryption_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'atrribute': 'SAI_MACSEC_SC_ATTR_ENCRYPTION_ENABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

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
                    'sai_macsec_cipher_suite_t',
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
