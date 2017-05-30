import os
import csv
from collections import namedtuple

import requests

APIKEY = os.environ['APIKEY']
URL = 'https://api.um.warszawa.pl/api/action/datastore_search/'


Resource = namedtuple('Resource', ['id_', 'name', 'limit', 'total'])

columns_assigned_list = []

BushesResource = Resource(id_='0b1af81f-247d-4266-9823-693858ad5b5d',
                          name='bushes',
                          limit=10000,
                          total=22123)

BushGroupsResource = Resource(id_='4b792a76-5349-4aad-aa16-dadaf0a74be3',
                              name='bush_groups',
                              limit=20000,
                              total=82200)

ForestsResource = Resource(id_='75bedfd5-6c83-426b-9ae5-f03651857a48',
                           name='forests',
                           limit=20000,
                           total=63286)

TreesResource = Resource(id_='ed6217dd-c8d0-4f7b-8bed-3b7eb81a95ba',
                         name='trees',
                         limit=30000,
                         total=139348)

TreeGroupsResource = Resource(id_='913856f7-f71b-4638-abe2-12df14334e1a',
                              name='tree_groups',
                              limit=20000,
                              total=29202)


def save_resources_to_csv(records, resource):
    with open(resource.name + '.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        if resource.name not in columns_assigned_list:
            columns_assigned_list.append(resource.name)
            csv_writer.writerow([k for k, v in records[0].items()])
        for rec in records:
            csv_writer.writerow([v for k, v in rec.items()])


def process_resource_data(resource):
    offset = 0

    while offset < resource.total:
        url = URL + '?resource_id={}&apikey={}&limit={}&offset={}'.format(
            resource.id_,
            APIKEY,
            resource.limit,
            offset
        )

        resp = requests.get(url)
        records = resp.json()['result']['records']
        save_resources_to_csv(records, resource=resource)

        offset += resource.limit

def main():
    resources = [BushesResource, BushGroupsResource, ForestsResource,
                 TreesResource, TreeGroupsResource]
    for resource in resources:
        process_resource_data(resource)

if __name__ == '__main__':
    main()
