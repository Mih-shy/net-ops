

# -*- coding: utf-8 -*-
'''
Задание 3.7
Преобразовать MAC-адрес в двоичную строку (без двоеточий).
'''
MAC = "AAAA:BBBB:CCCC"
MAC = bin(int(''.join(MAC.split(':')), 16))[2:]
print(MAC)
