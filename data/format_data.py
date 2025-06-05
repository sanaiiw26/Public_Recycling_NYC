#format_data.py
import csv
import json
from collections import defaultdict

input_csv = 'data/cleansed_recycling_data.csv'
output_json = 'data/data.json'

borough_bins = defaultdict(int)

with open(input_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            paper = int(row.get('Paper Bins', 0))
            mgp = int(row.get('MGP Bins', 0))
        except ValueError:
            paper = 0
            mgp = 0

        total = paper + mgp
        borough = row.get('DSNY Zone', 'Unknown')
        borough_bins[borough] += total

data = [
    {'borough': boro, 'total_bins': total}
    for boro, total in borough_bins.items()
]

with open(output_json, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=2)

print("✅ data.json successfully created.")
