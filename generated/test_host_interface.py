from pprint import pprint

import pytest


@pytest.mark.npu
class TestSaiHostInterface:
    # object with no attributes

    def test_host_interface_create(
        self,
    ):
        commands = [
            {
                'name': 'host_interface_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_HOST_INTERFACE',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_host_interface_remove(
        self,
    ):
        commands = [{'name': 'host_interface_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
