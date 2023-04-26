

from pprint import pprint

import pytest


class TestSaiNatZoneCounter:

    @pytest.mark.dependency(scope='session')
    def test_nat_zone_counter_create(self, npu):

        commands = [{'name': 'nat_zone_counter_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_nat_zone_counter_remove(self, npu):

        commands = [{'name': 'nat_zone_counter_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

