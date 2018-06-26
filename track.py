import requests
import json
import gzip
import sqlite3
import time

db = sqlite3.connect('./folitrack.sqlite3')
db.execute('CREATE TABLE IF NOT EXISTS track (id INTEGER PRIMARY KEY, timestamp INT, json_gz BLOB)')
resp = requests.get('http://data.foli.fi/citybike')
resp.raise_for_status()
data = resp.json()
bin_data = gzip.compress(json.dumps(data, sort_keys=True, ensure_ascii=False).encode('utf-8'))
db.execute('INSERT INTO track (timestamp, json_gz) VALUES (?, ?)', [time.time(), bin_data])
db.execute('COMMIT')