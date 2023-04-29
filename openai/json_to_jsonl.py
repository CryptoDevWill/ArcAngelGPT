import json

# Open the regular JSON file for reading
with open('tune.json', 'r') as input_file:
    # Load the JSON data from the file
    data = json.load(input_file)

# Open a new file for writing the JSONL data
with open('output.jsonl', 'w') as output_file:
    # Iterate over each JSON object in the data
    for obj in data:
        # Convert the object to a string and write to the output file
        output_file.write(json.dumps(obj) + '\n')
