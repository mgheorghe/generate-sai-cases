from pprint import pprint

import pytest


class TestSaiPortSerdes:
    # object with parent SAI_OBJECT_TYPE_PORT

    @pytest.mark.dependency(scope='session')
    def test_port_serdes_create(self, npu):
        commands = [
            {
                'name': 'port_serdes_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT_SERDES',
                'attributes': ['SAI_PORT_SERDES_ATTR_PORT_ID', 'sai_object_id_t'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_port_serdes_remove(self, npu):
        commands = [
            {
                'name': 'port_serdes_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT_SERDES',
                'attributes': ['SAI_PORT_SERDES_ATTR_PORT_ID', 'sai_object_id_t'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
