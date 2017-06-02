#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('CREATE TABLE autobusy (datetime text, dump text, t integer);')
conn.commit()
conn.close()
