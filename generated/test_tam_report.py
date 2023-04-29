from pprint import pprint

import pytest


class TestSaiTamReport:
    # object with no parents

    @pytest.mark.dependency(scope='session')
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

    def test_sai_tam_report_attr_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_TYPE', 'TODO'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_report_attr_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_tam_report_attr_quota_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_quota_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_QUOTA', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_report_attr_quota_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_quota_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_QUOTA',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_report_attr_report_interval_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_report_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_REPORT_INTERVAL', '1000'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_report_attr_report_interval_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_report_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_REPORT_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '1000' for result in results]), 'Get error'

    def test_sai_tam_report_attr_enterprise_number_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_enterprise_number_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_ENTERPRISE_NUMBER', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_report_attr_enterprise_number_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_enterprise_number_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_ENTERPRISE_NUMBER',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_tam_report_attr_template_report_interval_set(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_template_report_interval_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': ['SAI_TAM_REPORT_ATTR_TEMPLATE_REPORT_INTERVAL', '15'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_tam_report_attr_template_report_interval_get(self, dpu):
        commands = [
            {
                'name': 'sai_tam_report_attr_template_report_interval_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'atrribute': 'SAI_TAM_REPORT_ATTR_TEMPLATE_REPORT_INTERVAL',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '15' for result in results]), 'Get error'

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
