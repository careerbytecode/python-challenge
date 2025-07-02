import csv, os, sys, json
json_file = "sample.json"
output_file = "output.json"

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
        writer = json.dump(filtered_data, other_file)
