

from pprint import pprint

import pytest


class TestSaiVipEntry:

    @pytest.mark.dependency(scope='session')
    def test_vip_entry_create(self, npu):

        commands = [{'name': 'vip_entry_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_VIP_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_vip_entry_remove(self, npu):

        commands = [{'name': 'vip_entry_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_VIP_ENTRY', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

