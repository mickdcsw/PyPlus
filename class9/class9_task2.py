
from my_functions import open_napalm_connection
from my_functions import create_backup
from my_devices import all_devices
from napalm import get_network_driver
from pprint import pprint


for d in all_devices:
    connection = open_napalm_connection(d)
    arp_table = connection.get_arp_table()
    print('\n\nARP table for ',d['hostname'])
    pprint(arp_table)

    try:
        ntp_peers = connection.get_ntp_peers()
        print('\nNTP Peers for ',d['hostname'])
        pprint(ntp_peers)
    except:
        print('unable to show ntp_peers')

    create_backup(connection,d['hostname'])

