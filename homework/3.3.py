CONFIG = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlan = CONFIG.split()[-1]
vlan = vlan.split(',')
print(vlan)
