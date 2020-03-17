import json
import csv

f = open('test.json')
data = json.load(f)
f.close()

f = open('data.csv')
csv_file = csv.writer(f)

for item in data:
	f.writerow(item)

f.close()