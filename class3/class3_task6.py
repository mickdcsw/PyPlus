import yaml
from pprint import pprint
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

file = "/home/mwhite/.netmiko.yml"

with open(file) as f:
    yaml_out = yaml.load(f)

device = yaml_out["cisco4"]

with ConnectHandler(**device) as connected:
    output = connected.send_command('show run')

show_run_obj = CiscoConfParse(output.splitlines())

ints_w_ip = show_run_obj.find_objects_w_child(
    parentspec=r'^interface', childspec=r'^\s+ip address'
)


#pprint(ints_w_ip[0].children)

for item in ints_w_ip:
    print("Interface Line: {}".format(item.text)
    ip_addr = item.re_search_children(r'ip address')[0].text
    print("IP Address Line: {}".format(ip_addr))
    print()
print()



