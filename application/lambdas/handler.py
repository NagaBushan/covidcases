import json
import logging
import requests
import os
import csv
import boto3

logger = logging.getLogger('covid_new_cases')


def handle(event, context):
    print('Triggering handler..')
    # logger.info('Triggered scheduled batch to get the covid new cases')

    response = get_covid_cases()
    json_response = response.json()

    with open('covid.csv', 'r+b') as data_file:
        # json.dump(json_response['data'], file, indent=4)
        covid_json = json_response['data']

        csv_writer = csv.writer(data_file)

        count = 0
        for d in covid_json:
            if count ==0:
                header = d.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(d.values())
        # data_file.close()

    # logger.info('Scheduled job is completed')

    return "Covid data extracted successfully"


def get_covid_cases():
    api_url = os.environ['COVID_CASES_API']
    return requests.get(url=api_url)

def upload_into_s3():
    client = boto3.client("s3")


