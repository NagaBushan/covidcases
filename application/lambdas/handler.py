import json
import logging
import requests
import os

logger = logging.getLogger('covid_new_cases')


def handle(event, context):
    print('Triggering handler..')
    logger.info('Triggered scheduled batch to get the covid new cases')

    response = get_covid_cases()
    # json_response = response.json()
    with open('covid_cases.json', 'w') as file:
        json.dump(response, file, indent=4, sort_keys=True)

    logger.info('Scheduled job is completed')

    return response


def get_covid_cases():
    api = os.environ['COVID_CASES_API']
    url = api
    return requests.get(url)
