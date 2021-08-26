import yaml
from getpass import getpass

password = getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password
}

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclas",
    "password": password
}

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password
}

devices = [cisco3, cisco4, nxos1, nxos2]

filename = "class3_task2a.yaml"

with open(filename, "wt") as f:
    yaml.dump(devices, f, indent=4)

