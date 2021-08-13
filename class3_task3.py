import json

file = "interfaces.json"
v4ip_list = []
v6ip_list = []

# Open NAPALM output from nxos in JSON format
with open(file) as f:
    input = json.load(f)

# Drill down to IP address and prefix length, append list with both
for intf, ip_dict in input.items():
    for ipv, address in ip_dict.items():
        for ip, length in address.items():
            if ipv == "ipv4":
                mask = length["prefix_length"]
                v4ip_list.append("{}/{}".format(ip, mask))
            elif ipv == "ipv6":
                mask == length["prefix_length"]
                v6ip_list.append("{}/{}".format(ip, mask))

# Print IP list using 2 variations. 1st work though not sure why. Second was in solution.
print(v4ip_list)
print("\nIPv6 Addresses, {}\n".format(v6ip_list))

