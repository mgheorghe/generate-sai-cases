

from pprint import pprint

import pytest


class TestSaiFineGrainedHashField:

    @pytest.mark.dependency(scope='session')
    def test_fine_grained_hash_field_create(self, npu):

        commands = [{'name': 'fine_grained_hash_field_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_FINE_GRAINED_HASH_FIELD', 'attributes': ['SAI_FINE_GRAINED_HASH_FIELD_ATTR_IPV4_MASK', 'sai_ip4_t', 'SAI_FINE_GRAINED_HASH_FIELD_ATTR_IPV6_MASK', 'sai_ip6_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_fine_grained_hash_field_remove(self, npu):

        commands = [{'name': 'fine_grained_hash_field_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_FINE_GRAINED_HASH_FIELD', 'attributes': ['SAI_FINE_GRAINED_HASH_FIELD_ATTR_IPV4_MASK', 'sai_ip4_t', 'SAI_FINE_GRAINED_HASH_FIELD_ATTR_IPV6_MASK', 'sai_ip6_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

