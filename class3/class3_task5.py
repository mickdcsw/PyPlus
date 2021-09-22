import yaml
from pprint import pprint
from netmiko import ConnectHandler

file = "/home/mwhite/.netmiko.yml"

with open(file) as f:
    yaml_out = yaml.load(f)

device = yaml_out["cisco3"]

with ConnectHandler(**device) as connected:
    output = connected.find_prompt()

print(output)

