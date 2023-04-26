

from pprint import pprint

import pytest


class TestSaiHash:

    @pytest.mark.dependency(scope='session')
    def test_hash_create(self, npu):

        commands = [{'name': 'hash_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HASH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_hash_remove(self, npu):

        commands = [{'name': 'hash_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HASH', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

