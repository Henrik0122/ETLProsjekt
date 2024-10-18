# SNIPPET
for column, data_type in zip(columns, data_types):
    if "object" in str(data_type):  # Handling object (string) data type
        sql_query += f"    {column} TEXT,\n"
    elif "float" in str(data_type):  # Handling float data type
        sql_query += f"    {column} FLOAT,\n"
    elif "int" in str(data_type):  # Handling integer data type
        sql_query += f"    {column} INTEGER,\n"
    elif "date" in str(data_type):  # Handling datetime data type
        sql_query += f"    {column} DATE,\n"
    # Add more conditions like this if other data types are needed