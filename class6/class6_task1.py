import pyeapi

from pprint import pprint
from getpass import getpass

connect = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443"
)

device = pyeapi.client.Node(connect)

output = device.enable("show arp")

pprint(f"IP Addres: {output[0]['result']['ipV4Neighbors'][0]['address']} HW Address: {output[0]['result']['ipV4Neighbors'][0]['hwAddress']}")
