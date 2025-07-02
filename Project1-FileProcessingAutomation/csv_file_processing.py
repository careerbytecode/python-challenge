import csv, os, sys, json
csv_file = "sample.csv"
output_file = "output.csv"

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
