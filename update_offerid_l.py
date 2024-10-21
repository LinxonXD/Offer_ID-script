import json
import os

input_dir = "input"
output_dir = "output"

os.makedirs(output_dir, exist_ok=True)

input_file_path = os.path.join(input_dir, "FurnitureData.json")
output_file_path = os.path.join(output_dir, "FurnitureData.json")

with open(input_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

if "roomitemtypes" in data and "furnitype" in data["roomitemtypes"]:
    furnitypes = data["roomitemtypes"]["furnitype"]

    for item in furnitypes:
        if "id" in item:
            item["offerid"] = item["id"]

    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)

    print("Offer IDs have been updated to match IDs.")
else:
    print("Unexpected data format. Bruh wut?")