"""
Python solution for SiteHost Coding Challenge Part One - Calling an API

@author Shreyali Ganvir
Date    8th June 2024

"""

import requests
import os
from dotenv import load_dotenv
load_dotenv()


def create_url(endpoint):
    try:
        api_key = os.getenv("API_KEY")
        base_url = os.getenv("BASE_URL")
    except KeyError as e:
        raise e

    url = f"{base_url}/{endpoint}?api_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.json()


def main():

    # get domain names and zone ids
    zone_ids = []
    try:
        client_id = os.getenv("CLIENT_ID")
    except KeyError as e:
        raise e
    domain_json = create_url(f"domains/{client_id}")
    for each_domain in domain_json:
        print(f"Domain name : {each_domain['name']}")
        print(f"DNS zone for domain {each_domain['name']} : {each_domain['zones']}")
        for each_zone in each_domain['zones']:
            zone_ids.append(each_zone['uri'].split("/")[-1])
    # get DNS Records
    print("*"*200)
    for each_id in zone_ids:
        dns_records_json = create_url(f"zones/{each_id}")
        records = dns_records_json['records']
        print(f"DNS records for zone_id : {each_id} : {records}")


if __name__ == '__main__':
    main()
