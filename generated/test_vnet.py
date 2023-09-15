from pprint import pprint

import pytest


@pytest.mark.dpu
class TestSaiVnet:
    # object with no attributes

    def test_vnet_create(self, dpu):
        commands = [
            {
                'name': 'vnet_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VNET',
                'attributes': [],
            }
        ]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_vnet_attr_vni_set')
    def test_sai_vnet_attr_vni_set(self, dpu):
        commands = [
            {'name': 'vnet_1', 'op': 'set', 'attributes': ['SAI_VNET_ATTR_VNI', '0']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_vnet_attr_vni_set'])
    def test_sai_vnet_attr_vni_get(self, dpu):
        commands = [
            {'name': 'vnet_1', 'op': 'get', 'attributes': ['SAI_VNET_ATTR_VNI']}
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_vnet_remove(self, dpu):
        commands = [{'name': 'vnet_1', 'op': 'remove'}]

        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
