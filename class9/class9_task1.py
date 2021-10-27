#!/usr/bin/env python

from pprint import pprint
from napalm import get_network_driver
import my_devices

def task1b(dev):
    device_type = dev.pop("device_type")
    driver = get_network_driver(device_type)

    device = driver(**dev)   
    device.open()
    print(device,"\n")
    facts = device.get_facts()
    pprint(facts)
    print('\n')
    print('The Platform Type is:',device_type)


if __name__ == "__main__":

    #task1b(my_devices.cisco3)

    for d in my_devices.all_devices:
        task1b(d)
        
