from pprint import pprint

import pytest


class TestSaiArsProfile:
    # object with no attributes

    def test_ars_profile_create(self, npu):
        commands = [
            {
                'name': 'ars_profile_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_ars_profile_attr_algo_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_algo_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_ALGO', 'SAI_ARS_PROFILE_ALGO_EWMA'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_algo_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_algo_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_ALGO',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_ARS_PROFILE_ALGO_EWMA' for result in results]
        ), 'Get error'

    def test_sai_ars_profile_attr_sampling_interval_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_sampling_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_SAMPLING_INTERVAL', '16'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_sampling_interval_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_sampling_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_SAMPLING_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '16' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_ars_random_seed_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_ars_random_seed_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_ARS_RANDOM_SEED', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_ars_random_seed_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_ars_random_seed_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_ARS_RANDOM_SEED',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_ecmp_ars_max_groups_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_ecmp_ars_max_groups_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_ECMP_ARS_MAX_GROUPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_ecmp_ars_max_members_per_group_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_ecmp_ars_max_members_per_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_ECMP_ARS_MAX_MEMBERS_PER_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_lag_ars_max_groups_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_lag_ars_max_groups_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_LAG_ARS_MAX_GROUPS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_lag_ars_max_members_per_group_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_lag_ars_max_members_per_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_LAG_ARS_MAX_MEMBERS_PER_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_past_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_past_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_PORT_LOAD_PAST', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_past_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_past_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_PORT_LOAD_PAST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_past_weight_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_past_weight_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_PORT_LOAD_PAST_WEIGHT', '16'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_past_weight_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_past_weight_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_PORT_LOAD_PAST_WEIGHT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '16' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_future_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_future_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_PORT_LOAD_FUTURE', 'true'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_future_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_future_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_PORT_LOAD_FUTURE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'true' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_future_weight_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_future_weight_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_PORT_LOAD_FUTURE_WEIGHT', '16'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_future_weight_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_future_weight_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_PORT_LOAD_FUTURE_WEIGHT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '16' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_current_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_current_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_PORT_LOAD_CURRENT', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_current_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_current_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_PORT_LOAD_CURRENT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_exponent_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_exponent_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_PORT_LOAD_EXPONENT', '2'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_port_load_exponent_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_port_load_exponent_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_PORT_LOAD_EXPONENT',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '2' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_bands_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_bands_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BANDS',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_0_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_0_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_0_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_0_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_0_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_0_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_0_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_0_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_0_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_0_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_0_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_0_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_1_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_1_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_1_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_1_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_1_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_1_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_1_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_1_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_1_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_1_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_1_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_1_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_2_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_2_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_2_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_2_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_2_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_2_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_2_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_2_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_2_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_2_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_2_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_2_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_3_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_3_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_3_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_3_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_3_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_3_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_3_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_3_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_3_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_3_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_3_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_3_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_4_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_4_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_4_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_4_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_4_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_4_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_4_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_4_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_4_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_4_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_4_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_4_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_5_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_5_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_5_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_5_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_5_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_5_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_5_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_5_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_5_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_5_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_5_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_5_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_6_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_6_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_6_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_6_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_6_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_6_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_6_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_6_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_6_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_6_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_6_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_6_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_7_min_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_7_min_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_7_MIN_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_7_min_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_7_min_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_7_MIN_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_7_max_threshold_set(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_7_max_threshold_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': ['SAI_ARS_PROFILE_ATTR_QUANT_BAND_7_MAX_THRESHOLD', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_ars_profile_attr_quant_band_7_max_threshold_get(self, npu):
        commands = [
            {
                'name': 'sai_ars_profile_attr_quant_band_7_max_threshold_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'atrribute': 'SAI_ARS_PROFILE_ATTR_QUANT_BAND_7_MAX_THRESHOLD',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_ars_profile_remove(self, npu):
        commands = [
            {
                'name': 'ars_profile_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
