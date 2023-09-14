
from pprint import pprint

import pytest

@pytest.mark.
class TestSaiMax:
    # object with no attributes

    def test_max_create(self, ):

        commands = [{'name': 'max_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MAX', 'attributes': []}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    def test_max_remove(self, ):

        commands = [{'name': 'max_1', 'op': 'remove'}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

