from getpass import getpass

password = getpass()

cisco3 = dict(
    hostname="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    device_type="ios",
    optional_args={}
)

arista1 = dict(
    hostname="arista1.lasthop.io",
    username="pyclass",
    password=password,
    device_type="eos",
    optional_args={}
)

nxos1 = dict(
    hostname="nxos1.lasthop.io",
    username="pyclass",
    password=password,
    device_type="nx-os",
    optional_args={"port": 8443}

all_devices = [cisco3, arista1]
