from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiGenericProgrammable:
    # object with no parents

    def test_generic_programmable_create(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_GENERIC_PROGRAMMABLE',
                'attributes': ['SAI_GENERIC_PROGRAMMABLE_ATTR_OBJECT_NAME', '2:10,11'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    @pytest.mark.dependency(name='test_sai_generic_programmable_attr_entry_set')
    def test_sai_generic_programmable_attr_entry_set(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'set',
                'attributes': ['SAI_GENERIC_PROGRAMMABLE_ATTR_ENTRY', 'vendor'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_generic_programmable_attr_entry_set'])
    def test_sai_generic_programmable_attr_entry_get(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'get',
                'attributes': ['SAI_GENERIC_PROGRAMMABLE_ATTR_ENTRY'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'vendor', 'Get error, expected vendor but got %s' % r_value

    @pytest.mark.dependency(name='test_sai_generic_programmable_attr_counter_id_set')
    def test_sai_generic_programmable_attr_counter_id_set(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'set',
                'attributes': ['SAI_GENERIC_PROGRAMMABLE_ATTR_COUNTER_ID', 'null'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)

    @pytest.mark.dependency(
        depends=['test_sai_generic_programmable_attr_counter_id_set']
    )
    def test_sai_generic_programmable_attr_counter_id_get(self, npu):
        commands = [
            {
                'name': 'generic_programmable_1',
                'op': 'get',
                'attributes': ['SAI_GENERIC_PROGRAMMABLE_ATTR_COUNTER_ID'],
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

    def test_generic_programmable_remove(self, npu):
        commands = [{'name': 'generic_programmable_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
