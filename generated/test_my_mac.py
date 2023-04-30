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

    def test_sai_my_mac_attr_priority_set(self, npu):
        commands = [
            {
                'name': 'sai_my_mac_attr_priority_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_MAC',
                'atrribute': ['SAI_MY_MAC_ATTR_PRIORITY', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_my_mac_attr_priority_get(self, npu):
        commands = [
            {
                'name': 'sai_my_mac_attr_priority_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MY_MAC',
                'atrribute': 'SAI_MY_MAC_ATTR_PRIORITY',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

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
