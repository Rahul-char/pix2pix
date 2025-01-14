import os
import json

# Define folder paths
input_folder = "C:\\Users\\288032\\Documents\\LoginDataset\\Input"
output_folder = "C:\\Users\\288032\\Documents\\LoginDataset\\Output"
prompt_folder = "C:\\Users\\288032\\Documents\\LoginDataset\\Prompt"

# List all files in the folders
input_files = sorted(os.listdir(input_folder))
output_files = sorted(os.listdir(output_folder))
prompt_files = sorted(os.listdir(prompt_folder))

# Initialize the dataset
dataset = []

# Iterate through output and prompt files
for output_file, prompt_file in zip(output_files, prompt_files):
    # Extract the input file name prefix (e.g., '001' from '001_1.jpg')
    input_prefix = output_file.split('.')[0]
    input_file = f"{input_prefix}.0.jpeg"

    # Add a new entry for each output-prompt combination
    dataset.append({
        "input_image": f"{input_folder}\\{input_file}",
        "output_image": f"{output_folder}\\{output_file}",
        "prompt": open(os.path.join(prompt_folder, prompt_file)).read().strip()
    })

# Save to JSON file
output_json_path = "C:\\Users\\288032\\Documents\\LoginDataset\\dataset.json"
with open(output_json_path, "w") as json_file:
    json.dump(dataset, json_file, indent=4)

print(f"JSON file 'dataset.json' has been created at {output_json_path}!")
