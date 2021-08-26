
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

vars = {
    "interface_1": "Ethernet1/1",
    "ip_address_1": "10.1.100.1",
    "netmask_1": "/24",
    "interface_2": "Ethernet 1/1",
    "ip_address_2": "10.1.100.2",
    "netmask_2": "/24"
}

template_file = "class5_task2.j2"
template = env.get_template(template_file)
output = template.render(**vars)

print(output)
