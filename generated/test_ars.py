from pprint import pprint

import pytest


class TestSaiArs:
    # object with no attributes

    def test_ars_create(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_ars_attr_mode_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_mode_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_MODE', 'SAI_ARS_MODE_FLOWLET_QUALITY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_mode_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_mode_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_MODE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_ARS_MODE_FLOWLET_QUALITY' for result in results]
        ), 'Get error'

    def test_sai_ars_attr_idle_time_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_idle_time_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_IDLE_TIME', '256'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_idle_time_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_idle_time_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_IDLE_TIME',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '256' for result in results]), 'Get error'

    def test_sai_ars_attr_max_flows_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_max_flows_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_MAX_FLOWS', '512'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_max_flows_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_max_flows_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_MAX_FLOWS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '512' for result in results]), 'Get error'

    def test_sai_ars_attr_mon_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_mon_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_MON_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_mon_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_mon_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_MON_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_ars_attr_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_samplepacket_enable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_SAMPLEPACKET_ENABLE', 'SAI_NULL_OBJECT_ID'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_samplepacket_enable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_SAMPLEPACKET_ENABLE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_ars_attr_max_alt_memebers_per_group_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_max_alt_memebers_per_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_MAX_ALT_MEMEBERS_PER_GROUP', '16'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_max_alt_memebers_per_group_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_max_alt_memebers_per_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_MAX_ALT_MEMEBERS_PER_GROUP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '16' for result in results]), 'Get error'

    def test_sai_ars_attr_max_primary_memebers_per_group_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_max_primary_memebers_per_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_MAX_PRIMARY_MEMEBERS_PER_GROUP', '16'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_max_primary_memebers_per_group_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_max_primary_memebers_per_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_MAX_PRIMARY_MEMEBERS_PER_GROUP',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '16' for result in results]), 'Get error'

    def test_sai_ars_attr_primary_path_quality_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_primary_path_quality_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_PRIMARY_PATH_QUALITY_THRESHOLD', '16'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_primary_path_quality_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_primary_path_quality_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_PRIMARY_PATH_QUALITY_THRESHOLD',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '16' for result in results]), 'Get error'

    def test_sai_ars_attr_alternate_path_cost_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_alternate_path_cost_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_ALTERNATE_PATH_COST', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_alternate_path_cost_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_alternate_path_cost_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_ALTERNATE_PATH_COST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_attr_alternate_path_bias_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_alternate_path_bias_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': ['SAI_ARS_ATTR_ALTERNATE_PATH_BIAS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_attr_alternate_path_bias_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_attr_alternate_path_bias_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'atrribute': 'SAI_ARS_ATTR_ALTERNATE_PATH_BIAS',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_ars_remove(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ARS',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
