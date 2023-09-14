
from pprint import pprint

import pytest

@pytest.mark.
class TestSai60:
    # object with no attributes

    def test___60_create(self, ):

        commands = [{'name': '__60_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE___60', 'attributes': []}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    def test___60_remove(self, ):

        commands = [{'name': '__60_1', 'op': 'remove'}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

