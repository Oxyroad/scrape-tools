#!/usr/bin/env python3

import datetime
import sqlite3

import requests

APIKEY = ''
ENDPOINT = 'https://api.um.warszawa.pl/api/action/wsstore_get/?id=c7238cfe-8b1f-4c38-bb4a-de386db7e776&apikey={}'.format(APIKEY)
conn = sqlite3.connect('database.db')
c = conn.cursor()

date = str(datetime.datetime.now())
print('Getting data')
dump = requests.get(ENDPOINT).text

c.execute('insert into tramwaje values (?, ?)', (date, dump))
conn.commit()
conn.close()
print('Done.')
