import csv, os, sys, json

input_file = input("Enter the input CSV or JSON file name with absolute path: ").strip()
output_file = input("Enter the output CSV or JSON file name with absolute path: ").strip()

# Currently, using hardcoded 'name' and 'email' as filter columns

def csv_file_parsing(csv_file, output_file):
    '''This function parses a CSV file, filters the requested columns, and writes the output to another file.'''
    if not os.path.exists(csv_file):
        print(f"Error: The file {csv_file} does not exist.")
        sys.exit(1)

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        with open(output_file, 'w') as other_file:
            writer = csv.DictWriter(other_file, fieldnames=['name', 'email'])
            if other_file.tell() == 0:
                writer.writeheader()
            for row in reader:
                writer.writerow({'name': row['name'], 'email': row['email']})

def json_file_parsing(json_file, output_file):
    '''This function parses a JSON file, filters the requested columns, and writes the output to another file.'''
    if not os.path.exists(json_file):
        print(f"Error: The file {json_file} does not exist.")
        sys.exit(1)

    with open(json_file, mode='r') as file:
        reader = json.load(file)

    filtered_data = []
    for i in reader:
        data = {
            "name": i.get("name"),
            "email": i.get("email")
        }
        filtered_data.append(data)

    with open(output_file, 'w') as other_file:
        json.dump(filtered_data, other_file)

# Verify the file type using the file extension
if input_file.endswith('.csv'):
    csv_file_parsing(input_file, output_file)
elif input_file.endswith('.json'):
    json_file_parsing(input_file, output_file)
