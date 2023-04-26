

from pprint import pprint

import pytest


class TestSaiPolicer:

    @pytest.mark.dependency(scope='session')
    def test_policer_create(self, npu):

        commands = [{'name': 'policer_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_POLICER', 'attributes': ['SAI_POLICER_ATTR_METER_TYPE', 'sai_meter_type_t', 'SAI_POLICER_ATTR_MODE', 'sai_policer_mode_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_policer_remove(self, npu):

        commands = [{'name': 'policer_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_POLICER', 'attributes': ['SAI_POLICER_ATTR_METER_TYPE', 'sai_meter_type_t', 'SAI_POLICER_ATTR_MODE', 'sai_policer_mode_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

