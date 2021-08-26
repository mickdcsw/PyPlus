from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from class5_task3c_connect import nxos1, nxos2

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

nxos1_vars = {
    "device_name": "nxos1",
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.1",
    "netmask": "/24",
    "local_as": "22",
    "peer_ip": "10.1.100.2",
    "remote_as": "22"
}

nxos2_vars = {
    "device_name": "nxos2",
    "interface": "Ethernet 1/1",
    "ip_address": "10.1.100.2",
    "netmask": "/24",
    "local_as": "22",
    "peer_ip": "10.1.100.1",
    "remote_as": "22"
}

nxos1[config] = nxos1_vars
nxos2[config] = nxos2_vars

template_file = "class5_task2b.j2"
template = env.get_template(template_file)

for device in (nxos1, nxos2):
    with ConnectHandler(**nxos) as connect:
    output = template.render(**device[config])
    conf_out = connect.send_config(output)
    print(output)
