
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "password": "88newclass",
    "username": password,
    "device_type": "cisco_ios"
}

config = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

netconnect = ConnectHandler(**cisco3)
output = ""

with netconnect as connect:
    for item in config:
        output += connect.send_config_set(item)

    ping_response = connect.send_command("ping www.google.com") 

print(output)
print(ping_response)

