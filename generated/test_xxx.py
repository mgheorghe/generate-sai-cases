
from pprint import pprint

import pytest

@pytest.mark.
class TestSaiXxx:
    # object with no attributes

    def test_xxx_create(self, ):

        commands = [{'name': 'xxx_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_XXX', 'attributes': []}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    def test_xxx_remove(self, ):

        commands = [{'name': 'xxx_1', 'op': 'remove'}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

