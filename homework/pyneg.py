import os

ospf_r = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
out = """
Protocol:           {}
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
"""

ospf_r = ospf_r.split()[1:]
ospf_r.remove('via')
ospf_r.insert(0,'OSPF')
pr,pref,ad,nexth,last,outb = ospf_r
print(out.format(pr,pref,ad,nexth,last,outb))