from netmiko import ConnectHandler

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}

netconnect = ConnectHandler(**cisco4)

output = netconnect.send_command("ping", expect_string=r"Protocol", strip_prompt=False, strip_command=False)
output += netconnect.send_command("\n", expect_string=r"Target", strip_prompt=False, strip_command=False)
output += netconnect.send_command("8.8.8.8", expect_string=r"Repeat", strip_prompt=False, strip_command=False)
output += netconnect.send_command("\n", expect_string=r"Datagram", strip_prompt=False, strip_command=False)
output += netconnect.send_command("\n", expect_string=r"Timeout", strip_prompt=False, strip_command=False)
output += netconnect.send_command("\n", expect_string=r"Extended", strip_prompt=False, strip_command=False)
output += netconnect.send_command("\n", expect_string=r"Sweep", strip_prompt=False, strip_command=False)
output += netconnect.send_command("\n", expect_string=r"#", strip_prompt=False, strip_command=False)

print(output)

