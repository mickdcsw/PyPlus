from netmiko import ConnectHandler
from datetime  import datetime

nxos2 = {"host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios"
}


with ConnectHandler(**nxos2) as command:
    output = command.send_command("show version", use_textfsm=True)

print(output)

with ConnectHandler(**nxos2) as command:
    output2 = command.send_command("show lldp neighbors", use_textfsm=True)

print(output2)

#print(output[0][neighbor_interface])
