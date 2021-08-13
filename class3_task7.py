from ciscoconfparse import CiscoConfParse

bgp_conf = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""

bgp_peers = []

bgp_obj = CiscoConfParse(bgp_conf.splitlines())

bgp_nei_obj = bgp_obj.find_objects_w_parents(parentspec=r"^router",childspec=r"neighbor")

for neighbor in bgp_nei_obj:
    _, neighbor_ip = neighbor.text.split()
    for child in neighbor.children:
        if "remote-as" in child.text:
            _, remote_as = child.text.split()
    bgp_peers.append((neighbor_ip, remote_as))

print("BGP Peers:") 
print(bgp_peers)

