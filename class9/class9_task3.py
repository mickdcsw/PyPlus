from my_functions import open_napalm_connection
from my_devices import all_devices
from napalm import get_network_driver
from pprint import pprint

for d in all_devices:
    connection = open_napalm_connection(d)
    filename = f"{d['hostname']}-loopbacks"
    connection.load_merge_candidate(filename=filename)
    diff = connection.compare_config()
    print(f"\n**** candidate config diff for {d['hostname']}")
    pprint(diff)
    connection.commit_config()
    post_diff = connection.compare_config()
    print("** config diff post commit **")
    pprint(post_diff)
