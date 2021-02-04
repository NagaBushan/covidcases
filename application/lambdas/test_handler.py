import mock
from mock.mock import Mock, patch
from requests.api import get
from .handler import handle
import pytest
import os
from pytest_mock import mocker
import json
class TestHandler:
    @pytest.fixture
    def event(self):
        return None

    @pytest.fixture
    def context(self):
        return None


    @mock.patch.dict(os.environ, {'COVID_CASES_API': 'https://api.test/url'})
    def test_lambda_handler(self, event, context, mocker):
        # json_data = json.dumps({'status_code':200, 'message':'Got results'})
        json_data= {
            "data": [
                {
                    "date": "2021-02-04",
                    "newCases": 18529
                }]
        }
        mocker.patch('lambdas.handler.get_covid_cases', return_value = json.dumps(json_data))
        result = handle(event, context)
        print('result: ', type(result))
        # assert result == json_data
        # assert_valid_schema(result, 'vendor_list.json')
