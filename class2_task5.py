from netmiko import ConnectHandler

device1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos"
}

device2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos" 
}

def display_output(output):
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()

devices = [device1, device2]
config_file = "class2_task5_vlans.txt"

for device in devices:
    netconnect = ConnectHandler(**device) 
    output = ""
    with netconnect as connect:
        output += connect.send_config_from_file(config_file)
        connect.save_config()
    print(device["host"], output)
    display_output(output)

