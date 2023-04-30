from pprint import pprint

import pytest


class TestSaiNatZoneCounter:
    # object with no attributes

    def test_nat_zone_counter_create(self, npu):
        commands = [
            {
                'name': 'nat_zone_counter_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_nat_zone_counter_attr_nat_type_set(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_nat_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': [
                    'SAI_NAT_ZONE_COUNTER_ATTR_NAT_TYPE',
                    'SAI_NAT_TYPE_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_nat_type_get(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_nat_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': 'SAI_NAT_ZONE_COUNTER_ATTR_NAT_TYPE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NAT_TYPE_NONE' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_zone_id_set(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_zone_id_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': ['SAI_NAT_ZONE_COUNTER_ATTR_ZONE_ID', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_zone_id_get(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_zone_id_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': 'SAI_NAT_ZONE_COUNTER_ATTR_ZONE_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_discard_packet_count_set(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_discard_packet_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': ['SAI_NAT_ZONE_COUNTER_ATTR_DISCARD_PACKET_COUNT', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_discard_packet_count_get(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_discard_packet_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': 'SAI_NAT_ZONE_COUNTER_ATTR_DISCARD_PACKET_COUNT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_translation_needed_packet_count_set(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_translation_needed_packet_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': [
                    'SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATION_NEEDED_PACKET_COUNT',
                    '0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_translation_needed_packet_count_get(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_translation_needed_packet_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': 'SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATION_NEEDED_PACKET_COUNT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_translations_packet_count_set(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_translations_packet_count_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': [
                    'SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATIONS_PACKET_COUNT',
                    '0',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_nat_zone_counter_attr_translations_packet_count_get(self, npu):
        commands = [
            {
                'name': 'sai_nat_zone_counter_attr_translations_packet_count_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'atrribute': 'SAI_NAT_ZONE_COUNTER_ATTR_TRANSLATIONS_PACKET_COUNT',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_nat_zone_counter_remove(self, npu):
        commands = [
            {
                'name': 'nat_zone_counter_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_NAT_ZONE_COUNTER',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
