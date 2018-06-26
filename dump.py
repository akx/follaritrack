import requests
import json
import gzip
import sqlite3
import time

db = sqlite3.connect('./folitrack.sqlite3')
c = db.cursor()
c.execute('SELECT timestamp, json_gz FROM track')
for row in c:
    timestamp, gz_data = row
    data = json.loads(gzip.decompress(gz_data), encoding='utf-8')
    print(data)