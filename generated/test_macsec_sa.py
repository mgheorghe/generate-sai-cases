from pprint import pprint

import pytest


class TestSaiMacsecSa:
    # object with parent SAI_OBJECT_TYPE_MACSEC_SC

    @pytest.mark.dependency(scope='session')
    def test_macsec_sa_create(self, npu):
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
            {
                'name': 'macsec_sa_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SA',
                'attributes': [
                    'SAI_MACSEC_SA_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_SA_ATTR_SC_ID',
                    '$macsec_sc_1',
                    'SAI_MACSEC_SA_ATTR_AN',
                    'sai_uint8_t',
                    'SAI_MACSEC_SA_ATTR_SAK',
                    'sai_macsec_sak_t',
                    'SAI_MACSEC_SA_ATTR_SALT',
                    'sai_macsec_salt_t',
                    'SAI_MACSEC_SA_ATTR_AUTH_KEY',
                    'sai_macsec_auth_key_t',
                    'SAI_MACSEC_SA_ATTR_MACSEC_SSCI',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_macsec_sa_remove(self, npu):
        commands = [
            {
                'name': 'macsec_sa_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SA',
                'attributes': [
                    'SAI_MACSEC_SA_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_SA_ATTR_SC_ID',
                    '$macsec_sc_1',
                    'SAI_MACSEC_SA_ATTR_AN',
                    'sai_uint8_t',
                    'SAI_MACSEC_SA_ATTR_SAK',
                    'sai_macsec_sak_t',
                    'SAI_MACSEC_SA_ATTR_SALT',
                    'sai_macsec_salt_t',
                    'SAI_MACSEC_SA_ATTR_AUTH_KEY',
                    'sai_macsec_auth_key_t',
                    'SAI_MACSEC_SA_ATTR_MACSEC_SSCI',
                    '10',
                ],
            },
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
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
