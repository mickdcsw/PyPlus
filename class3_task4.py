import json
from pprint import pprint

file = "arp_output.json"
addresses = {}

# Open the JSON file
with open(file) as f:
    data_input = json.load(f)

# Assign the dictionary item with key "ipV4Neighbors" to neighbros
neighbors = data_input["ipV4Neighbors"]

# Iterate over the list and find keys and assign value to variable
for item in neighbors:
    ip = item["address"]
    mac = item["hwAddress"]
    addresses[ip] = mac

pprint(addresses)
print()
print(addresses)

