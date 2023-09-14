
from pprint import pprint

import pytest

@pytest.mark.
class TestSaiExtensionsRangeStart:
    # object with no attributes

    def test_extensions_range_start_create(self, ):

        commands = [{'name': 'extensions_range_start_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_START', 'attributes': []}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)



    def test_extensions_range_start_remove(self, ):

        commands = [{'name': 'extensions_range_start_1', 'op': 'remove'}]

        results = [*.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

