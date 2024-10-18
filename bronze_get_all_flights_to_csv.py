import csv
import requests
import xml.etree.ElementTree as ET

def fetch_xml_to_csv(api_url, csv_filename):
    # Fetch data from the API URL
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML content from the response
        tree = ET.ElementTree(ET.fromstring(response.content))
        root = tree.getroot()

        # Open a CSV file for writing
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            # Create a CSV writer object
            csvwriter = csv.writer(csvfile)

            # Initialize a flag to write headers only once
            headers_written = False

            # Iterate through each 'flight' element and write to CSV
            for flight in root.findall('.//flight'):
                row_data = {sub_element.tag: sub_element.text for sub_element in flight}

                # Write headers if not already done
                if not headers_written:
                    headers = row_data.keys()
                    csvwriter.writerow(headers)
                    headers_written = True

                # Write the data row
                csvwriter.writerow(row_data.values())

        print(f"Data written to {csv_filename}")
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")

# Example usage with an API URL
time_from = '100'
time_to = '7'
d_airport = 'OSL'
lastUpdate = '2009-03-10T15:03:00Z'
api_url = f"https://flydata.avinor.no/XmlFeed.asp?TimeFrom={time_from}&TimeTo={time_to}&airport={d_airport}&direction=D&lastUpdate={lastUpdate}" 
csv_file_path = "bronze/flights.csv"


fetch_xml_to_csv(api_url, csv_file_path)