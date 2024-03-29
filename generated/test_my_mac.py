from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiMyMac:
    # object with no attributes

    def test_my_mac_create(self, npu):
        commands = [
            {
                'name': 'my_mac_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MY_MAC',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_my_mac_attr_priority_set')
    def test_sai_my_mac_attr_priority_set(self, npu):
        commands = [
            {
                'name': 'my_mac_1',
                'op': 'set',
                'attributes': ['SAI_MY_MAC_ATTR_PRIORITY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_my_mac_attr_priority_set'])
    def test_sai_my_mac_attr_priority_get(self, npu):
        commands = [
            {
                'name': 'my_mac_1',
                'op': 'get',
                'attributes': ['SAI_MY_MAC_ATTR_PRIORITY'],
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

    def test_my_mac_remove(self, npu):
        commands = [{'name': 'my_mac_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
