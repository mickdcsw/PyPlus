import time
import textfsm

from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from class5_task2c_connect import nxos1, nxos2

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

nxos1_vars = {
    "device_name": "nxos1",
    "interface": "Ethernet1/2",
    "ip_address": "10.1.120.1",
    "netmask": "/24",
    "local_as": "22",
    "peer_ip": "10.1.120.2",
    "remote_as": "22"
}

nxos2_vars = {
    "device_name": "nxos2",
    "interface": "Ethernet 1/2",
    "ip_address": "10.1.120.2",
    "netmask": "/24",
    "local_as": "22",
    "peer_ip": "10.1.120.1",
    "remote_as": "22"
}

nxos1["config"] = nxos1_vars
nxos2["config"] = nxos2_vars

template_file = "class5_task2b.j2"
template = env.get_template(template_file)
tfsm_temp_file = "class5_task2c.tpl"

for device in (nxos1, nxos2):
    tmp_device = device.copy()
    config_vars = tmp_device.pop("config")
    config_raw = template.render(**config_vars) 
    config = [config_raw.strip() for config_raw in config_raw.splitlines()]
    netconnect = ConnectHandler(**tmp_device)
    device["ssh_conn"] = netconnect
    conf_out = netconnect.send_config_set(config)

time.sleep(15)

for device in (nxos1, nxos2):
    ping = f"ping {device['config']['peer_ip']}"
    print(ping.center(80,'#'))
    ping_response = netconnect.send_command(ping)
    print(ping_response)
    sh_bgp =  f"show ip bgp summary | i {device['config']['peer_ip']}" 
    bgp_output = netconnect.send_command(sh_bgp)
    print(bgp_output)



for device in (nxos1, nxos2):
    netconnect = device["ssh_conn"]
    netconnect.disconnect()


