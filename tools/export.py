import csv
import json

with open('test.json') as json_file:
	data = json.load(json_file)

trace_data = data['traceObj']

data_file = open('testing.csv','w')

csv_writer = csv.writer(data_file)

count = 0

for trace in trace_data:
	if count == 0:
		header = trace.keys()
		csv_writer.writerow(header)
		count += 1
	csv_writer.writerow(trace.values())

data_file.close()

