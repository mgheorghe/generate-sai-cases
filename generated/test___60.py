from pprint import pprint


class TestSai60:
    # object with no attributes

    def test___60_create(self, npu):
        commands = [
            {
                'name': '__60_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE___60',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test___60_remove(self, npu):
        commands = [{'name': '__60_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
