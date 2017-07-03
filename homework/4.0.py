net =input('Введите сеть : ')
a , b , c , d , msk = [int(net1) for net1 in net.replace('/','.').split('.')] 
print('network:\n {:10} {:15} {:15} {:15}'.format(a,b,c,d))
print('\n      {:>10b} {:15b}          {:>08b}       {:>08b}'.format(a,b,c,d))