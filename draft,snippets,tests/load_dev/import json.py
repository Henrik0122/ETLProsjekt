import json

data = {
    "host": "summer22data.postgres.database.azure.com",
    "user": "student_marius",
    "password": "marius",
    "port": 5432,
    "db_name": "daily_marius"
}

# Specify the file path for the JSON file
json_file_path = "database_config.json"

# Write the data to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON data has been written to {json_file_path}")
