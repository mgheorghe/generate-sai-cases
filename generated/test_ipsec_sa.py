from pprint import pprint

import pytest


class TestSaiIpsecSa:
    # object with parent SAI_OBJECT_TYPE_IPSEC

    @pytest.mark.dependency(scope='session')
    def test_ipsec_sa_create(self, npu):
        commands = [
            {
                'name': 'ipsec_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'attributes': ['SAI_IPSEC_ATTR_EXTERNAL_SA_INDEX_ENABLE', 'True'],
            },
            {
                'name': 'ipsec_sa_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'attributes': [
                    'SAI_IPSEC_SA_ATTR_IPSEC_DIRECTION',
                    'sai_ipsec_direction_t',
                    'SAI_IPSEC_SA_ATTR_IPSEC_ID',
                    '$ipsec_1',
                    'SAI_IPSEC_SA_ATTR_IPSEC_SPI',
                    '10',
                    'SAI_IPSEC_SA_ATTR_ENCRYPT_KEY',
                    'sai_encrypt_key_t',
                    'SAI_IPSEC_SA_ATTR_SALT',
                    '10',
                    'SAI_IPSEC_SA_ATTR_AUTH_KEY',
                    'sai_auth_key_t',
                    'SAI_IPSEC_SA_ATTR_TERM_DST_IP',
                    'sai_ip_address_t',
                    'SAI_IPSEC_SA_ATTR_TERM_VLAN_ID',
                    '10',
                    'SAI_IPSEC_SA_ATTR_TERM_SRC_IP',
                    'sai_ip_address_t',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_ipsec_sa_remove(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'attributes': [
                    'SAI_IPSEC_SA_ATTR_IPSEC_DIRECTION',
                    'sai_ipsec_direction_t',
                    'SAI_IPSEC_SA_ATTR_IPSEC_ID',
                    '$ipsec_1',
                    'SAI_IPSEC_SA_ATTR_IPSEC_SPI',
                    '10',
                    'SAI_IPSEC_SA_ATTR_ENCRYPT_KEY',
                    'sai_encrypt_key_t',
                    'SAI_IPSEC_SA_ATTR_SALT',
                    '10',
                    'SAI_IPSEC_SA_ATTR_AUTH_KEY',
                    'sai_auth_key_t',
                    'SAI_IPSEC_SA_ATTR_TERM_DST_IP',
                    'sai_ip_address_t',
                    'SAI_IPSEC_SA_ATTR_TERM_VLAN_ID',
                    '10',
                    'SAI_IPSEC_SA_ATTR_TERM_SRC_IP',
                    'sai_ip_address_t',
                ],
            },
            {
                'name': 'ipsec_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'attributes': ['SAI_IPSEC_ATTR_EXTERNAL_SA_INDEX_ENABLE', 'True'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Remove error'
