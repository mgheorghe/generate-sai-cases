from pprint import pprint

import pytest


class TestSaiTamMathFunc:
    # object with no attributes

    def test_tam_math_func_create(self, npu):
        commands = [
            {
                'name': 'tam_math_func_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_MATH_FUNC',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency(
        name='test_sai_tam_math_func_attr_tam_tel_math_func_type_set'
    )
    def test_sai_tam_math_func_attr_tam_tel_math_func_type_set(self, npu):
        commands = [
            {
                'name': 'tam_math_func_1',
                'op': 'set',
                'attributes': [
                    'SAI_TAM_MATH_FUNC_ATTR_TAM_TEL_MATH_FUNC_TYPE',
                    'SAI_TAM_TEL_MATH_FUNC_TYPE_NONE',
                ],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_math_func_attr_tam_tel_math_func_type_set']
    )
    def test_sai_tam_math_func_attr_tam_tel_math_func_type_get(self, npu):
        commands = [
            {
                'name': 'tam_math_func_1',
                'op': 'get',
                'attributes': ['SAI_TAM_MATH_FUNC_ATTR_TAM_TEL_MATH_FUNC_TYPE'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == 'SAI_TAM_TEL_MATH_FUNC_TYPE_NONE', (
            'Get error, expected SAI_TAM_TEL_MATH_FUNC_TYPE_NONE but got %s' % r_value
        )

    def test_tam_math_func_remove(self, npu):
        commands = [{'name': 'tam_math_func_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
