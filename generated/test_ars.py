from pprint import pprint

import pytest


@pytest.mark.npu
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

    @pytest.mark.dependency(name='test_sai_ars_attr_mode_set')
    def test_sai_ars_attr_mode_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_MODE', 'SAI_ARS_MODE_FLOWLET_QUALITY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_ars_attr_mode_set'])
    def test_sai_ars_attr_mode_get(self, npu):
        commands = [{'name': 'ars_1', 'op': 'get', 'attributes': ['SAI_ARS_ATTR_MODE']}]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_ARS_MODE_FLOWLET_QUALITY', (
            'Get error, expected SAI_ARS_MODE_FLOWLET_QUALITY but got %s' % r_value
        )

    @pytest.mark.dependency(name='test_sai_ars_attr_idle_time_set')
    def test_sai_ars_attr_idle_time_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_IDLE_TIME', '256'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_ars_attr_idle_time_set'])
    def test_sai_ars_attr_idle_time_get(self, npu):
        commands = [
            {'name': 'ars_1', 'op': 'get', 'attributes': ['SAI_ARS_ATTR_IDLE_TIME']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '256', 'Get error, expected 256 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_max_flows_set')
    def test_sai_ars_attr_max_flows_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_MAX_FLOWS', '512'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_ars_attr_max_flows_set'])
    def test_sai_ars_attr_max_flows_get(self, npu):
        commands = [
            {'name': 'ars_1', 'op': 'get', 'attributes': ['SAI_ARS_ATTR_MAX_FLOWS']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '512', 'Get error, expected 512 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_mon_enable_set')
    def test_sai_ars_attr_mon_enable_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_MON_ENABLE', 'false'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_ars_attr_mon_enable_set'])
    def test_sai_ars_attr_mon_enable_get(self, npu):
        commands = [
            {'name': 'ars_1', 'op': 'get', 'attributes': ['SAI_ARS_ATTR_MON_ENABLE']}
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'false', 'Get error, expected false but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_samplepacket_enable_set')
    def test_sai_ars_attr_samplepacket_enable_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_SAMPLEPACKET_ENABLE', 'null'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_ars_attr_samplepacket_enable_set'])
    def test_sai_ars_attr_samplepacket_enable_get(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'get',
                'attributes': ['SAI_ARS_ATTR_SAMPLEPACKET_ENABLE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'null', 'Get error, expected null but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_max_alt_memebers_per_group_set')
    def test_sai_ars_attr_max_alt_memebers_per_group_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_MAX_ALT_MEMEBERS_PER_GROUP', '16'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_ars_attr_max_alt_memebers_per_group_set']
    )
    def test_sai_ars_attr_max_alt_memebers_per_group_get(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'get',
                'attributes': ['SAI_ARS_ATTR_MAX_ALT_MEMEBERS_PER_GROUP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '16', 'Get error, expected 16 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_max_primary_memebers_per_group_set')
    def test_sai_ars_attr_max_primary_memebers_per_group_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_MAX_PRIMARY_MEMEBERS_PER_GROUP', '16'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_ars_attr_max_primary_memebers_per_group_set']
    )
    def test_sai_ars_attr_max_primary_memebers_per_group_get(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'get',
                'attributes': ['SAI_ARS_ATTR_MAX_PRIMARY_MEMEBERS_PER_GROUP'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '16', 'Get error, expected 16 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_primary_path_quality_threshold_set')
    def test_sai_ars_attr_primary_path_quality_threshold_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_PRIMARY_PATH_QUALITY_THRESHOLD', '16'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_ars_attr_primary_path_quality_threshold_set']
    )
    def test_sai_ars_attr_primary_path_quality_threshold_get(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'get',
                'attributes': ['SAI_ARS_ATTR_PRIMARY_PATH_QUALITY_THRESHOLD'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '16', 'Get error, expected 16 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_alternate_path_cost_set')
    def test_sai_ars_attr_alternate_path_cost_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_ALTERNATE_PATH_COST', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_ars_attr_alternate_path_cost_set'])
    def test_sai_ars_attr_alternate_path_cost_get(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'get',
                'attributes': ['SAI_ARS_ATTR_ALTERNATE_PATH_COST'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_ars_attr_alternate_path_bias_set')
    def test_sai_ars_attr_alternate_path_bias_set(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'set',
                'attributes': ['SAI_ARS_ATTR_ALTERNATE_PATH_BIAS', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_ars_attr_alternate_path_bias_set'])
    def test_sai_ars_attr_alternate_path_bias_get(self, npu):
        commands = [
            {
                'name': 'ars_1',
                'op': 'get',
                'attributes': ['SAI_ARS_ATTR_ALTERNATE_PATH_BIAS'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value

    def test_ars_remove(self, npu):
        commands = [{'name': 'ars_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
