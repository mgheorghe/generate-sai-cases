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

    def test_sai_vnet_attr_vni_set(self, npu):
        commands = [
            {
                'name': 'sai_vnet_attr_vni_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VNET',
                'atrribute': ['SAI_VNET_ATTR_VNI', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_vnet_attr_vni_get(self, npu):
        commands = [
            {
                'name': 'sai_vnet_attr_vni_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_VNET',
                'atrribute': 'SAI_VNET_ATTR_VNI',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

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
