import csv
from collections import defaultdict
try:
	columns = defaultdict(list)
	with open('change.csv') as f:
		reader = csv.DictReader(f)
		for row in reader:
			for k, v in row.items():
				columns[k].append(v)
	print(columns['Name Of the Product'][:25])
except Exception as e:
	raise e