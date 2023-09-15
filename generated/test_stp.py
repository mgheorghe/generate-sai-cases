from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiStp:
    # object with no attributes

    def test_stp_create(self, npu):
        commands = [
            {
                'name': 'stp_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_STP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_sai_stp_attr_vlan_list_get(self, npu):
        commands = [
            {'name': 'stp_1', 'op': 'get', 'attributes': ['SAI_STP_ATTR_VLAN_LIST']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_stp_attr_bridge_id_get(self, npu):
        commands = [
            {'name': 'stp_1', 'op': 'get', 'attributes': ['SAI_STP_ATTR_BRIDGE_ID']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_sai_stp_attr_port_list_get(self, npu):
        commands = [
            {'name': 'stp_1', 'op': 'get', 'attributes': ['SAI_STP_ATTR_PORT_LIST']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' % r_value

    def test_stp_remove(self, npu):
        commands = [{'name': 'stp_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
