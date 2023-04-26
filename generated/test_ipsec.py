

from pprint import pprint

import pytest


class TestSaiIpsec:

    @pytest.mark.dependency(scope='session')
    def test_ipsec_create(self, npu):

        commands = [{'name': 'ipsec_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_IPSEC', 'attributes': ['SAI_IPSEC_ATTR_EXTERNAL_SA_INDEX_ENABLE', 'bool']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_ipsec_remove(self, npu):

        commands = [{'name': 'ipsec_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_IPSEC', 'attributes': ['SAI_IPSEC_ATTR_EXTERNAL_SA_INDEX_ENABLE', 'bool']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

