import csv
import sys

with open(sys.argv[1], 'r') as f:
	reader=csv.DictReader(f)
	for row in reader:
		print row

