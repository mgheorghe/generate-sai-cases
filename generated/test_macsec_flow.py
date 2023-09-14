
from pprint import pprint

import pytest

@pytest.mark.npu
class TestSaiMacsecFlow:
    # object with no parents

    def test_macsec_flow_create(self, npu):

        commands = [{'name': 'macsec_flow_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW', 'attributes': ['SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION', 'SAI_MACSEC_DIRECTION_EGRESS']}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    
    def test_sai_macsec_flow_attr_acl_entry_list_get(self, npu):

        commands = [
            {
                "name": "macsec_flow_1",
                "op": "get",
                "attributes": ["SAI_MACSEC_FLOW_ATTR_ACL_ENTRY_LIST"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    
    def test_sai_macsec_flow_attr_sc_list_get(self, npu):

        commands = [
            {
                "name": "macsec_flow_1",
                "op": "get",
                "attributes": ["SAI_MACSEC_FLOW_ATTR_SC_LIST"]
            }
        ]
        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values get =======")
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'TODO', 'Get error, expected TODO but got %s' %  r_value


    def test_macsec_flow_remove(self, npu):

        commands = [{'name': 'macsec_flow_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

