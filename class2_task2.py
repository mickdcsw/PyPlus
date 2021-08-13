from netmiko import ConnectHandler
from datetime  import datetime

nxos2 = {"host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}
print("********* Start Time ***********\n", datetime.now())

with ConnectHandler(**nxos2) as command:
    output = command.send_command("show lldp neighbors detail")

print("********* Global Delay 2 ********\n", datetime.now(), "\n", output)

with ConnectHandler(**nxos2) as command:
    output2 = command.send_command("show lldp neighbors detail", delay_factor=8)

print("********* Delay Factor 8 ******** \n", datetime.now(), "\n", output2)

