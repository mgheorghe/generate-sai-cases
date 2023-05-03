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

    @pytest.mark.dependency()
    def test_sai_vnet_attr_vni_set(self, npu):
        commands = [
            {
                'name': 'vnet_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VNET',
                'atrribute': ['SAI_VNET_ATTR_VNI', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_vnet_attr_vni_set'])
    def test_sai_vnet_attr_vni_get(self, npu):
        commands = [
            {
                'name': 'vnet_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VNET',
                'atrribute': 'SAI_VNET_ATTR_VNI',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    def test_vnet_remove(self, npu):
        commands = [
            {
                'name': 'vnet_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VNET',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
