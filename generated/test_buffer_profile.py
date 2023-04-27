

from pprint import pprint

import pytest

# object with parent SAI_OBJECT_TYPE_BUFFER_POOL
class TestSaiBufferProfile:

    @pytest.mark.dependency(scope='session')
    def test_buffer_profile_create(self, npu):

        commands = [{'name': 'buffer_profile_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_BUFFER_PROFILE', 'attributes': ['SAI_BUFFER_PROFILE_ATTR_POOL_ID', 'sai_object_id_t', 'SAI_BUFFER_PROFILE_ATTR_RESERVED_BUFFER_SIZE', '10', 'SAI_BUFFER_PROFILE_ATTR_THRESHOLD_MODE', 'sai_buffer_profile_threshold_mode_t', 'SAI_BUFFER_PROFILE_ATTR_SHARED_DYNAMIC_TH', 'sai_int8_t', 'SAI_BUFFER_PROFILE_ATTR_SHARED_STATIC_TH', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)
        assert all(results), "Create error"

    def test_buffer_profile_remove(self, npu):

        commands = [{'name': 'buffer_profile_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_BUFFER_PROFILE', 'attributes': ['SAI_BUFFER_PROFILE_ATTR_POOL_ID', 'sai_object_id_t', 'SAI_BUFFER_PROFILE_ATTR_RESERVED_BUFFER_SIZE', '10', 'SAI_BUFFER_PROFILE_ATTR_THRESHOLD_MODE', 'sai_buffer_profile_threshold_mode_t', 'SAI_BUFFER_PROFILE_ATTR_SHARED_DYNAMIC_TH', 'sai_int8_t', 'SAI_BUFFER_PROFILE_ATTR_SHARED_STATIC_TH', '10']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)
        assert all( [result == 'SAI_STATUS_SUCCESS' for result in results]), "Remove error"

