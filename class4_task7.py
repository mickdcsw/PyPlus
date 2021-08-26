#!/usr/bin/env python

import textfsm
from pprint import pprint

text_output = 'class4_task1.txt'
template_file = 'class4_task2.tpl'
interfaces = []

with open(text_output) as F, open(template_file) as template:
    output = F.read()

    re_table = textfsm.TextFSM(template)
    data = re_table.ParseText(output)
    header = re_table.header

    for item in data:
        fsm_dict = dict(zip(header,item))
        interfaces.append(fsm_dict)


pprint(interfaces)


