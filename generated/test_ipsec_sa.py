

from pprint import pprint

import pytest

# object with no attributes
class TestSaiIpsecSa:

    @pytest.mark.dependency(scope='session')
    def test_ipsec_sa_create(self, npu):

        commands = [{'name': 'ipsec_sa_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_IPSEC_SA', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_ipsec_sa_remove(self, npu):

        commands = [{'name': 'ipsec_sa_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_IPSEC_SA', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

