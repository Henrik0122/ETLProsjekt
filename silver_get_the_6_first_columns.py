def extract_first_six_columns(input_file_path, output_file_path):
    
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # Splitting each line into columns
            columns = line.strip().split(',')

            # Taking only the first 6 columns
            first_six_columns = columns[:6]

            # Writing the first 6 columns to the new file
            output_file.write(','.join(first_six_columns) + '\n')

    return output_file_path

# Example usage of the function
input_path = 'bronze/flights.csv'
output_path = 'silver/updated_flights.csv'
extract_first_six_columns(input_path, output_path)