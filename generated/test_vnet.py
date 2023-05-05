from pprint import pprint

import pytest


class TestSaiVnet:
    # object with no attributes

    def test_vnet_create(self, npu):
        commands = [
            {
                'name': 'vnet_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VNET',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(name='test_sai_vnet_attr_vni_set')
    def test_sai_vnet_attr_vni_set(self, npu):
        commands = [
            {'name': 'vnet_1', 'op': 'set', 'attributes': ['SAI_VNET_ATTR_VNI', '0']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vnet_attr_vni_set'])
    def test_sai_vnet_attr_vni_get(self, npu):
        commands = [
            {'name': 'vnet_1', 'op': 'get', 'attributes': ['SAI_VNET_ATTR_VNI']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_vnet_remove(self, npu):
        commands = [{'name': 'vnet_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
