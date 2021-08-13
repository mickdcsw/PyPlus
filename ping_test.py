from netmiko import ConnectHandler

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios"
}

output = ""

net_connect =  ConnectHandler(**cisco4)
commands = ["ping", "\n", "8.8.8.8", "\n", "\n", "\n", "\n", "\n"]

for command in commands:
    output += net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)

print(output)

net_connect.disconnect()
