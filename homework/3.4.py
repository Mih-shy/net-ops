command1 ="swithport trunk allowd vlan 1,3,10,20,30,100"
command2 ="swithport trunk allowd vlan 1,3,100,200,300"

command2 = set(command2.split()[-1].split(','))
command1 = set(command1.split()[-1].split(','))
uniq =list(command1.intersection(command2))
print(uniq)
