#!/usr/bin/env python3

import datetime
import sqlite3

import requests

APIKEY = ''
for t in [1, 2]:
    ENDPOINT = 'https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=%20f2e5503e-%0A927d-4ad3-9500-4ab9e55deb59&apikey={}&type={}'.format(APIKEY, t)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    date = str(datetime.datetime.now())
    print('Getting data')
    dump = requests.get(ENDPOINT).text

    c.execute('insert into autobusy values (?, ?, ?)', (date, dump, t))
    conn.commit()
    conn.close()
    print('Done.')
