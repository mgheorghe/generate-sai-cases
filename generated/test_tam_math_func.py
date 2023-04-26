

from pprint import pprint

import pytest


class TestSaiTamMathFunc:

    @pytest.mark.dependency(scope='session')
    def test_tam_math_func_create(self, npu):

        commands = [{'name': 'tam_math_func_1', 'op': 'create', 'type': 'SAI_OBJECT_TYPE_TAM_MATH_FUNC', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values create =======")
        pprint(results)

    def test_tam_math_func_remove(self, npu):

        commands = [{'name': 'tam_math_func_1', 'op': 'remove', 'type': 'SAI_OBJECT_TYPE_TAM_MATH_FUNC', 'attributes': []}]

        results = [*npu.process_commands(commands)]
        print("======= SAI commands RETURN values remove =======")
        pprint(results)

