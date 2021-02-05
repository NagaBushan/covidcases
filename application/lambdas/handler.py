import json
import logging
import requests
import os
import csv
import boto3
from requests.api import head
import datetime

logger = logging.getLogger('covid_new_cases')
FILE_NAME = 'covid.csv'

def handle(event, context):
    print('Calling handler..')
    # logger.info('Triggered scheduled batch to get the covid new cases')

    response = get_covid_cases()
    json_response = response.json()

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w'): pass

    with open(FILE_NAME, 'r+') as data_file:
        # json.dump(json_response['data'], file, indent=4)
        covid_json = json_response['data']

        csv_writer = csv.writer(data_file)

        count = 0
        for d in covid_json:
            if count ==0:
                header = d.keys()
                print(header)
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(d.values())
        # data_file.close()
        data_file  = sorted(data_file, key = lambda row: datetime.strptime(row[0], "%d-%b-%y"))

    # logger.info('Scheduled job is completed')

    return "Covid data extracted successfully"


def get_covid_cases():
    api_url = os.environ['COVID_CASES_API']
    return requests.get(url=api_url)

def upload_into_s3():
    client = boto3.client("s3")


