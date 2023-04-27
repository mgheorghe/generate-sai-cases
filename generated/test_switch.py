from pprint import pprint

import pytest


class TestSaiSwitch:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_switch_create(self, npu):
        commands = [
            {
                'name': 'switch_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'attributes': [
                    'SAI_SWITCH_ATTR_INIT_SWITCH',
                    'bool',
                    'SAI_SWITCH_ATTR_HARDWARE_ACCESS_BUS',
                    'sai_switch_hardware_access_bus_t',
                    'SAI_SWITCH_ATTR_PLATFROM_CONTEXT',
                    'sai_uint64_t',
                    'SAI_SWITCH_ATTR_REGISTER_READ',
                    'sai_pointer_t sai_switch_register_read_fn',
                    'SAI_SWITCH_ATTR_REGISTER_WRITE',
                    'sai_pointer_t sai_switch_register_write_fn',
                    'SAI_SWITCH_ATTR_SWITCH_ID',
                    'sai_uint32_t',
                    'SAI_SWITCH_ATTR_MAX_SYSTEM_CORES',
                    'sai_uint32_t',
                    'SAI_SWITCH_ATTR_SYSTEM_PORT_CONFIG_LIST',
                    'sai_system_port_config_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_switch_remove(self, npu):
        commands = [
            {
                'name': 'switch_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_SWITCH',
                'attributes': [
                    'SAI_SWITCH_ATTR_INIT_SWITCH',
                    'bool',
                    'SAI_SWITCH_ATTR_HARDWARE_ACCESS_BUS',
                    'sai_switch_hardware_access_bus_t',
                    'SAI_SWITCH_ATTR_PLATFROM_CONTEXT',
                    'sai_uint64_t',
                    'SAI_SWITCH_ATTR_REGISTER_READ',
                    'sai_pointer_t sai_switch_register_read_fn',
                    'SAI_SWITCH_ATTR_REGISTER_WRITE',
                    'sai_pointer_t sai_switch_register_write_fn',
                    'SAI_SWITCH_ATTR_SWITCH_ID',
                    'sai_uint32_t',
                    'SAI_SWITCH_ATTR_MAX_SYSTEM_CORES',
                    'sai_uint32_t',
                    'SAI_SWITCH_ATTR_SYSTEM_PORT_CONFIG_LIST',
                    'sai_system_port_config_list_t',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
