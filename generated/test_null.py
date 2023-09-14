
from pprint import pprint

import pytest

@pytest.mark.
class TestSaiNull:
    # object with no attributes

    def test_null_create(self, ):

        commands = [{'name': 'null_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_NULL', 'attributes': []}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    def test_null_remove(self, ):

        commands = [{'name': 'null_1', 'op': 'remove'}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

