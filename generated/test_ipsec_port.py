from pprint import pprint

import pytest


class TestSaiIpsecPort:
    # object with parent SAI_OBJECT_TYPE_PORT

    @pytest.mark.dependency(scope='session')
    def test_ipsec_port_create(self, npu):
        commands = [
            {
                'name': 'ipsec_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'attributes': [
                    'SAI_IPSEC_PORT_ATTR_PORT_ID',
                    'sai_object_id_t',
                    'SAI_IPSEC_PORT_ATTR_NATIVE_VLAN_ID',
                    '10',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_ipsec_port_remove(self, npu):
        commands = [
            {
                'name': 'ipsec_port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_IPSEC_PORT',
                'attributes': [
                    'SAI_IPSEC_PORT_ATTR_PORT_ID',
                    'sai_object_id_t',
                    'SAI_IPSEC_PORT_ATTR_NATIVE_VLAN_ID',
                    '10',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
