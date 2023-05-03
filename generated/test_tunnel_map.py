from pprint import pprint


class TestSaiTunnelMap:
    # object with no parents

    def test_tunnel_map_create(self, npu):
        commands = [
            {
                'name': 'tunnel_map_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP',
                'attributes': [
                    'SAI_TUNNEL_MAP_ATTR_TYPE',
                    'SAI_TUNNEL_MAP_TYPE_OECN_TO_UECN',
                ],
                'key': {'key': 'TODO', 'value': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_tunnel_map_attr_entry_list_get(self, npu):
        commands = [
            {
                'name': 'tunnel_map_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP',
                'atrribute': 'SAI_TUNNEL_MAP_ATTR_ENTRY_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_tunnel_map_remove(self, npu):
        commands = [
            {
                'name': 'tunnel_map_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TUNNEL_MAP',
                'attributes': [
                    'SAI_TUNNEL_MAP_ATTR_TYPE',
                    'SAI_TUNNEL_MAP_TYPE_OECN_TO_UECN',
                ],
                'key': {'key': 'TODO', 'value': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
