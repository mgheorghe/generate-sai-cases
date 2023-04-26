

from pprint import pprint

import pytest


class TestSaiSamplepacket:

    @pytest.mark.dependency(scope='session')
    def test_samplepacket_create(self, npu):

        commands = [{'name': 'samplepacket_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_SAMPLEPACKET', 'attributes': ['SAI_SAMPLEPACKET_ATTR_SAMPLE_RATE', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_samplepacket_remove(self, npu):

        commands = [{'name': 'samplepacket_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_SAMPLEPACKET', 'attributes': ['SAI_SAMPLEPACKET_ATTR_SAMPLE_RATE', 'sai_uint32_t']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
