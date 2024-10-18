import json
import csv

def get_api_key(filename):
    with open(filename, 'r') as file:
        file_contents = file.read()
    return file_contents

def import_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
    

def converter(file1, file2):
    with open(file1, 'r') as json_file:
        data = json.load(json_file)
        csv_file = file2

    with open(csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data[0].keys())

        for row in data:
            csv_writer.writerow(row.values())

    return csv_file

def csv_to_json(file1, file2):
    csv_file_path = file1
    json_file_path = file2
    
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)
