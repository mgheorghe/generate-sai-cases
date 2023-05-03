from pprint import pprint

import pytest


class TestSaiSamplepacket:
    # object with no parents

    def test_samplepacket_create(self, npu):
        commands = [
            {
                'name': 'samplepacket_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SAMPLEPACKET',
                'attributes': ['SAI_SAMPLEPACKET_ATTR_SAMPLE_RATE', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_samplepacket_attr_sample_rate_set(self, npu):
        commands = [
            {
                'name': 'samplepacket_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SAMPLEPACKET',
                'atrribute': ['SAI_SAMPLEPACKET_ATTR_SAMPLE_RATE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_samplepacket_attr_sample_rate_set'])
    def test_sai_samplepacket_attr_sample_rate_get(self, npu):
        commands = [
            {
                'name': 'samplepacket_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_SAMPLEPACKET',
                'atrribute': 'SAI_SAMPLEPACKET_ATTR_SAMPLE_RATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_samplepacket_remove(self, npu):
        commands = [
            {
                'name': 'samplepacket_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SAMPLEPACKET',
                'attributes': ['SAI_SAMPLEPACKET_ATTR_SAMPLE_RATE', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
