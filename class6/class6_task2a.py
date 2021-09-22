import pyeapi
import yaml
from pprint import pprint
from getpass import getpass

arp_map = []

def load_device(filename):
    with open(filename) as file:
        return yaml.safe_load(file)
    raise ValueError("Reading YAML file failed")


def main():
    device_dict = load_device("class6_task2a.yml")
    device_dict['password'] = getpass()
    connection = pyeapi.client.connect(**device_dict)
    command = "show arp"
    device = pyeapi.client.Node(connection)
    output = device.enable(command)
    neighbors = output[0]['result']['ipV4Neighbors']
    for neighbor in neighbors:
        address = neighbor['address']
        mac = neighbor['hwAddress']
        map = {}
        map['ip'] = address
        map['mac'] = mac
        arp_map.append(map)
        pprint(f"IP Address: {address}   MAC Address:{mac}")
    pprint(arp_map) 

if __name__ == "__main__":
    main()
