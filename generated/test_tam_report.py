from pprint import pprint

import pytest


class TestSaiTamReport:
    # object with no parents

    def test_tam_report_create(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_tam_report_attr_type_set(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_TYPE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_report_attr_type_set'])
    def test_sai_tam_report_attr_type_get(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_TYPE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_report_attr_quota_set(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_QUOTA', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_report_attr_quota_set'])
    def test_sai_tam_report_attr_quota_get(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_QUOTA',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_report_attr_report_interval_set(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_REPORT_INTERVAL', '1000'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_report_attr_report_interval_set'])
    def test_sai_tam_report_attr_report_interval_get(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_REPORT_INTERVAL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '1000', (
            'Get error, expected 1000 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_report_attr_enterprise_number_set(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_ENTERPRISE_NUMBER', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_tam_report_attr_enterprise_number_set'])
    def test_sai_tam_report_attr_enterprise_number_get(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_ENTERPRISE_NUMBER',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_tam_report_attr_template_report_interval_set(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_TEMPLATE_REPORT_INTERVAL', '15'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(
        depends=['test_sai_tam_report_attr_template_report_interval_set']
    )
    def test_sai_tam_report_attr_template_report_interval_get(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_TEMPLATE_REPORT_INTERVAL',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '15', (
            'Get error, expected 15 but got %s' % results[1][0].value()
        )

    def test_tam_report_remove(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
