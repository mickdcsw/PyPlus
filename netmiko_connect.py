#!/usr/bin/env python

from netmiko import ConnectHandler
#from getpass import getpasss

device1 = {"host": "cisco3.lasthop.io",
	"username": "pyclass",
	"password": "88newclass",
	"device_type": "cisco_ios",
	"session_log": "last_session_log.txt"
	}

	
device2 = {"host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": "88newclass",
        "device_type": "cisco_ios",
        "session_log": "last_session_log.txt"
        }

device_list = [device1, device2]

for device in device_list:
	net_connect = ConnectHandler(**device)
	print(net_connect.find_prompt())

net_connect2 = ConnectHandler(**device1)
show_ver = net_connect2.send_command("show version")
print(show_ver)


