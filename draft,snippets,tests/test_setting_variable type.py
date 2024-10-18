import pandas as pd

# Updated Sample DataFrame
data = {
    'col1': ['abc', 'defgh', 'ijklmn', 'opqrs', 'tuvwx'],
    'col2': [1.1, 2.2, 3.3, 4.4, 5.5],
    'col3': [10, 20, 30, 40, 50],
    'col4': pd.to_datetime(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']),
    'col5': [0.1, 123.45, 1e-3, 1e38, -1.5],
    'col6': [0.001, 678.9, 2e-4, 9.99e37, -123.45],
}

df = pd.DataFrame(data)

# Function to estimate the appropriate size for each data type
def estimate_column_size(column):
    if df[column].dtype == 'O':  # Handling object (string) data type
        max_length = df[column].str.len().max()
        return f"{column} VARCHAR({max_length})"
    elif df[column].dtype == 'float64':  # Handling float data type
        max_value = df[column].max()
        if max_value < 1e-3:
            return f"{column} FLOAT"
        elif max_value < 1e38:
            return f"{column} REAL"
        else:
            return f"{column} DOUBLE"
    elif df[column].dtype == 'int64':  # Handling integer data type
        max_value = df[column].max()
        if max_value < 256:
            return f"{column} TINYINT"
        elif max_value < 65536:
            return f"{column} SMALLINT"
        elif max_value < 4294967296:
            return f"{column} INT"
        else:
            return f"{column} BIGINT"
    elif df[column].dtype == 'datetime64[ns]':  # Handling datetime data type
        return f"{column} DATE"

# Create SQL query
sql_query = "CREATE TABLE your_table_name (\n"
for column in df.columns:
    column_definition = estimate_column_size(column)
    if column_definition is not None:
        sql_query += "    " + column_definition + ",\n"

sql_query = sql_query.rstrip(",\n")  # Remove trailing comma and newline
sql_query += "\n);"

print(sql_query)
