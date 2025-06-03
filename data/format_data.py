# format_data.py

import csv
import json

input_file = 'data/cleansed_recycling_data.csv'
output_file = 'data/data.json'

def csv_to_json(csv_path, json_path):
    data = []

    with open(csv_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    with open(json_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    csv_to_json(input_file, output_file)
    print(f"Converted {input_file} to {output_file}")
