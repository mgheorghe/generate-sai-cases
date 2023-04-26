

from pprint import pprint

import pytest


class TestSaiNatEntry:

    @pytest.mark.dependency(scope='session')
    def test_nat_entry_create(self, npu):

        commands = [{'name': 'nat_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NAT_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_nat_entry_remove(self, npu):

        commands = [{'name': 'nat_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_NAT_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

