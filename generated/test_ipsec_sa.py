from pprint import pprint

import pytest


class TestSaiIpsecSa:
    # object with parent SAI_OBJECT_TYPE_IPSEC

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
                    'SAI_IPSEC_DIRECTION_EGRESS',
                    'SAI_IPSEC_SA_ATTR_IPSEC_ID',
                    '$ipsec_1',
                    'SAI_IPSEC_SA_ATTR_IPSEC_SPI',
                    '10',
                    'SAI_IPSEC_SA_ATTR_ENCRYPT_KEY',
                    'typedef UINT8   sai_encrypt_key_t[32]',
                    'SAI_IPSEC_SA_ATTR_SALT',
                    '10',
                    'SAI_IPSEC_SA_ATTR_AUTH_KEY',
                    'typedef UINT8   sai_auth_key_t[16]',
                    'SAI_IPSEC_SA_ATTR_TERM_DST_IP',
                    '180.0.0.1',
                    'SAI_IPSEC_SA_ATTR_TERM_VLAN_ID',
                    '10',
                    'SAI_IPSEC_SA_ATTR_TERM_SRC_IP',
                    '180.0.0.1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_ipsec_sa_attr_octet_count_status_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_OCTET_COUNT_STATUS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipsec_sa_attr_external_sa_index_set(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': ['SAI_IPSEC_SA_ATTR_EXTERNAL_SA_INDEX', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipsec_sa_attr_external_sa_index_set'])
    def test_sai_ipsec_sa_attr_external_sa_index_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_EXTERNAL_SA_INDEX',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    def test_sai_ipsec_sa_attr_sa_index_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_SA_INDEX',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipsec_sa_attr_ipsec_port_list_set(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': ['SAI_IPSEC_SA_ATTR_IPSEC_PORT_LIST', 'empty'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipsec_sa_attr_ipsec_port_list_set'])
    def test_sai_ipsec_sa_attr_ipsec_port_list_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_IPSEC_PORT_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'empty', (
            'Get error, expected empty but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipsec_sa_attr_ipsec_replay_protection_enable_set(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': [
                    'SAI_IPSEC_SA_ATTR_IPSEC_REPLAY_PROTECTION_ENABLE',
                    'false',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_ipsec_sa_attr_ipsec_replay_protection_enable_set']
    )
    def test_sai_ipsec_sa_attr_ipsec_replay_protection_enable_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_IPSEC_REPLAY_PROTECTION_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'false', (
            'Get error, expected false but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipsec_sa_attr_ipsec_replay_protection_window_set(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': ['SAI_IPSEC_SA_ATTR_IPSEC_REPLAY_PROTECTION_WINDOW', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_ipsec_sa_attr_ipsec_replay_protection_window_set']
    )
    def test_sai_ipsec_sa_attr_ipsec_replay_protection_window_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_IPSEC_REPLAY_PROTECTION_WINDOW',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipsec_sa_attr_egress_esn_set(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': ['SAI_IPSEC_SA_ATTR_EGRESS_ESN', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipsec_sa_attr_egress_esn_set'])
    def test_sai_ipsec_sa_attr_egress_esn_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_EGRESS_ESN',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_ipsec_sa_attr_minimum_ingress_esn_set(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': ['SAI_IPSEC_SA_ATTR_MINIMUM_INGRESS_ESN', '1'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_ipsec_sa_attr_minimum_ingress_esn_set'])
    def test_sai_ipsec_sa_attr_minimum_ingress_esn_get(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'atrribute': 'SAI_IPSEC_SA_ATTR_MINIMUM_INGRESS_ESN',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '1', (
            'Get error, expected 1 but got %s' % results[1][0].value()
        )

    def test_ipsec_sa_remove(self, npu):
        commands = [
            {
                'name': 'ipsec_sa_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'attributes': [
                    'SAI_IPSEC_SA_ATTR_IPSEC_DIRECTION',
                    'SAI_IPSEC_DIRECTION_EGRESS',
                    'SAI_IPSEC_SA_ATTR_IPSEC_ID',
                    '$ipsec_1',
                    'SAI_IPSEC_SA_ATTR_IPSEC_SPI',
                    '10',
                    'SAI_IPSEC_SA_ATTR_ENCRYPT_KEY',
                    'typedef UINT8   sai_encrypt_key_t[32]',
                    'SAI_IPSEC_SA_ATTR_SALT',
                    '10',
                    'SAI_IPSEC_SA_ATTR_AUTH_KEY',
                    'typedef UINT8   sai_auth_key_t[16]',
                    'SAI_IPSEC_SA_ATTR_TERM_DST_IP',
                    '180.0.0.1',
                    'SAI_IPSEC_SA_ATTR_TERM_VLAN_ID',
                    '10',
                    'SAI_IPSEC_SA_ATTR_TERM_SRC_IP',
                    '180.0.0.1',
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
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
