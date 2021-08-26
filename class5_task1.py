#!/usr/bin/env python

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from jinja2 import Template

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

bgp_template = """
router bgp {{ local_as }}
 neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
  update-source loopback99
  ebgp-multihop 2
  address-family ipv4 unicast
 neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
  address-family ipv4 unicast
"""

bgp_vars = {
    "local_as": "20",
    "peer1_ip": "10.1.20.2",
    "peer1_as": "20",
    "peer2_ip": "10.1.30.1",
    "peer2_as": "30",
}

#template = env.get_template(bgp_template)
template = Template(bgp_template)
output = template.render(**bgp_vars)

print(output)
