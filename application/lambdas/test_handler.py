import boto3
import mock
from mock.mock import Mock, patch
from requests.api import get
from .handler import handle, upload_file_into_s3
import pytest
import os
from pytest_mock import mocker
import json
from moto import mock_s3
import filecmp

class TestHandler:
    @pytest.fixture
    def event(self):
        return None

    @pytest.fixture
    def context(self):
        return None

    s3_test_data = 'test_data/downloaded_s3_test.csv'
    test_file = "test_data/test.csv"

    @pytest.mark.skip
    @mock.patch.dict(os.environ, {'COVID_CASES_API': 'https://api.test/url'})
    def test_lambda_handler(self, event, context, mocker):
        data= '{ "data": [ { "date": "2021-1-1", "newCases": 18529 }] }'
        json_data = json.loads(data)
        mocker.patch('lambdas.handler.get_covid_cases', return_value = json_data)
        result = handle(event, context)
        print('result: ', result)
        # assert result == json_data

    @mock_s3
    def test_upload_file_into_s3(self):
        # 1.Prep
        s3_client = boto3.resource("s3", region_name = "eu-west-2")
        bucket = s3_client.Bucket('covid-cases')
        bucket.create(
            ACL="public-read", CreateBucketConfiguration={"LocationConstraint": "eu-west-2"}
        )
        open(self.s3_test_data, 'w').close()

        # 2.Act
        upload_file_into_s3(self.test_file)

        # 3.Assert
        s3_client.Object('covid-cases', self.test_file).download_file(self.s3_test_data)

        assert filecmp.cmp(self.s3_test_data, self.test_file)
