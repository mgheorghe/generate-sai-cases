

from pprint import pprint

import pytest


class TestSaiHostif:

    @pytest.mark.dependency(scope='session')
    def test_hostif_create(self, npu):

        commands = [{'name': 'hostif_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_HOSTIF', 'attributes': ['SAI_HOSTIF_ATTR_TYPE', 'sai_hostif_type_t', 'SAI_HOSTIF_ATTR_OBJ_ID', 'sai_object_id_t', 'SAI_HOSTIF_ATTR_NAME', 'char', 'SAI_HOSTIF_ATTR_GENETLINK_MCGRP_NAME', 'char']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_hostif_remove(self, npu):

        commands = [{'name': 'hostif_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_HOSTIF', 'attributes': ['SAI_HOSTIF_ATTR_TYPE', 'sai_hostif_type_t', 'SAI_HOSTIF_ATTR_OBJ_ID', 'sai_object_id_t', 'SAI_HOSTIF_ATTR_NAME', 'char', 'SAI_HOSTIF_ATTR_GENETLINK_MCGRP_NAME', 'char']}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

