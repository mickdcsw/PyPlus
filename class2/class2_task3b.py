from netmiko import ConnectHandler
from datetime  import datetime
from getpass import getpass

password = getpass()

router = {"host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios"
}


with ConnectHandler(**router) as command:
    output2 = command.send_command("show lldp neighbors", use_textfsm=True)

print(output2)

print(output2[0]['neighbor_interface'])
