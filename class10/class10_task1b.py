from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from my_devices import all_devices
from datetime import datetime


def connector(device, command):
    with ConnectHandler(**device) as connect:
        output = connect.send_command(command)
        return output


if __name__ == "__main__":

    start_time = datetime.now()

    for device in all_devices:
        optional_args = device.pop("optional_args")
        print(f"#### Command started for {device['host']} at {datetime.now()}")
        output = connector(device, "show version")
        print(output)
        print(f"#### Command finished for {device['host']} at {datetime.now()}\n")

    print(f"#### Job was completed in {str(datetime.now() - start_time)}")
