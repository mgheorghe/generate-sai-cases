from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiMacsecSa:
    # object with parent SAI_OBJECT_TYPE_MACSEC_SC

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
                    'SAI_MACSEC_CIPHER_SUITE_GCM_AES_128',
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
                    '1',
                    'SAI_MACSEC_SA_ATTR_SAK',
                    'typedef UINT8   sai_macsec_sak_t[32]',
                    'SAI_MACSEC_SA_ATTR_SALT',
                    'typedef UINT8   sai_macsec_salt_t[12]',
                    'SAI_MACSEC_SA_ATTR_AUTH_KEY',
                    'typedef UINT8   sai_macsec_auth_key_t[16]',
                    'SAI_MACSEC_SA_ATTR_MACSEC_SSCI',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_macsec_sa_attr_configured_egress_xpn_set')
    def test_sai_macsec_sa_attr_configured_egress_xpn_set(self, npu):
        commands = [
            {
                'name': 'macsec_sa_1',
                'op': 'set',
                'attributes': ['SAI_MACSEC_SA_ATTR_CONFIGURED_EGRESS_XPN', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_macsec_sa_attr_configured_egress_xpn_set']
    )
    def test_sai_macsec_sa_attr_configured_egress_xpn_get(self, npu):
        commands = [
            {
                'name': 'macsec_sa_1',
                'op': 'get',
                'attributes': ['SAI_MACSEC_SA_ATTR_CONFIGURED_EGRESS_XPN'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_sai_macsec_sa_attr_current_xpn_get(self, npu):
        commands = [
            {
                'name': 'macsec_sa_1',
                'op': 'get',
                'attributes': ['SAI_MACSEC_SA_ATTR_CURRENT_XPN'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_macsec_sa_attr_minimum_ingress_xpn_set')
    def test_sai_macsec_sa_attr_minimum_ingress_xpn_set(self, npu):
        commands = [
            {
                'name': 'macsec_sa_1',
                'op': 'set',
                'attributes': ['SAI_MACSEC_SA_ATTR_MINIMUM_INGRESS_XPN', '1'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_macsec_sa_attr_minimum_ingress_xpn_set'])
    def test_sai_macsec_sa_attr_minimum_ingress_xpn_get(self, npu):
        commands = [
            {
                'name': 'macsec_sa_1',
                'op': 'get',
                'attributes': ['SAI_MACSEC_SA_ATTR_MINIMUM_INGRESS_XPN'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '1', 'Get error, expected 1 but got %s' % r_value

    def test_macsec_sa_remove(self, npu):
        commands = [
            {'name': 'macsec_sa_1', 'op': 'remove'},
            {'name': 'macsec_sc_1', 'op': 'remove'},
            {'name': 'macsec_flow_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
