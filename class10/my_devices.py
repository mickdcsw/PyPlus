from getpass import getpass

password = getpass()
delay_factor = 4

cisco3 = dict(
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    device_type="cisco_ios",
    optional_args={}
)
arista1 = dict(
    host="arista1.lasthop.io",
    username="pyclass",
    password=password,
    device_type="arista_eos",
    global_delay_factor=delay_factor,
    optional_args={}
)
arista2 = dict(
    host="arista2.lasthop.io",
    username="pyclass",
    password=password,
    device_type="arista_eos",
    global_delay_factor=delay_factor,
    optional_args={}
)
srx2 = dict(
    host="srx2.lasthop.io",
    username="pyclass",
    password=password,
    device_type="juniper_junos",
    optional_args={}
)

all_devices = [cisco3,arista1,arista2,srx2]
