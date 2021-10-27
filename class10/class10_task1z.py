from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from my_devices import all_devices
from datetime import datetime


def connector(devices):
    with ConnectHandler(**device) as connect:
        output = connect.send_command("show version")
        return output


if __name__ == "__main__":

    start_time = datetime.now()
    max_threads = 4


    with ThreadPoolExecutor(max_threads) as pool:
        results = pool.map(connector, all_devices)
        print(results)
