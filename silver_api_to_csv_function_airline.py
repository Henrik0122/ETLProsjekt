import csv
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import get_api_key as gak
def fetch_xml_to_csv(api_url, csv_filename):

    # Fetch data from URL
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        tree = ET.ElementTree(ET.fromstring(response.content))
        root = tree.getroot()

        # Open a CSV file for writing
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer object
            csvwriter = csv.writer(csvfile)

            # Write CSV headers (assuming the first element has all possible attributes)
            headers = root[0].keys()
            csvwriter.writerow(headers)

            # Iterate through each XML element and write to CSV
            for child in root:
                row = [child.get(header) for header in headers]
                csvwriter.writerow(row)
        
        print(f"Data written to {csv_filename}")
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")

# Example usage
fetch_xml_to_csv("https://flydata.avinor.no/airlineNames.asp", "bronze/airline_names.csv")

def csv_to_json(csv_file_path, json_file_path):
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Convert the DataFrame to a JSON file
    df.to_json(json_file_path, orient='records', lines=False)

# Example usage of the function
csv_to_json('bronze/airline_names.csv', 'silver/airline_names.json')