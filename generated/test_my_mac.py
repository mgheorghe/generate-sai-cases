from pprint import pprint

import pytest


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
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_my_mac_attr_priority_set(self, npu):
        commands = [
            {
                'name': 'my_mac_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_MAC',
                'atrribute': ['SAI_MY_MAC_ATTR_PRIORITY', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_my_mac_attr_priority_set'])
    def test_sai_my_mac_attr_priority_get(self, npu):
        commands = [
            {
                'name': 'my_mac_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_MAC',
                'atrribute': 'SAI_MY_MAC_ATTR_PRIORITY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    def test_my_mac_remove(self, npu):
        commands = [
            {
                'name': 'my_mac_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MY_MAC',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
