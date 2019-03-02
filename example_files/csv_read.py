import csv
from pprint import pprint as pprint

with open('example.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pprint(row)
        print("\n")