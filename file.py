import os
import json
from collections import defaultdict

# Define folder paths
input_folder = "C:\\Users\\288032\\Documents\\LoginDataset\\Input"
output_folder = "C:\\Users\\288032\\Documents\\LoginDataset\\Output"
prompt_folder = "C:\\Users\\288032\\Documents\\LoginDataset\\Prompt"

# List all files
input_files = sorted(os.listdir(input_folder))
output_files = sorted(os.listdir(output_folder))
prompt_files = sorted(os.listdir(prompt_folder))

# Group outputs and prompts by input file
grouped_data = defaultdict(list)

for output_file, prompt_file in zip(output_files, prompt_files):
    # Extract input file prefix from output file (e.g., '001' from '001_1.jpg')
    input_prefix = output_file.split('.')[0]
    grouped_data[input_prefix].append({
        "output_image": f"{output_folder}\\{output_file}",
        "prompt": open(os.path.join(prompt_folder, prompt_file)).read().strip()
    })

# Build the JSON structure
dataset = []
for input_file in input_files:

    input_prefix = input_file.split('.')[0]
    dataset.append({
        "input_image": f"{input_folder}\\{input_file}",
        "outputs": grouped_data.get(input_prefix, [])
    })

# Save to JSON file
with open("dataset.json", "w") as json_file:
    json.dump(dataset, json_file, indent=4)

print("JSON file 'dataset.json' has been created!")
