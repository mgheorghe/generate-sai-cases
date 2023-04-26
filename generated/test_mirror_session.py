

from pprint import pprint

import pytest

# object with no attributes
class TestSaiMirrorSession:

    @pytest.mark.dependency(scope='session')
    def test_mirror_session_create(self, npu):

        commands = [{'name': 'mirror_session_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_mirror_session_remove(self, npu):

        commands = [{'name': 'mirror_session_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_MIRROR_SESSION', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 0 for result in results]), "Remove error"

