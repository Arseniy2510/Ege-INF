from ipaddress import *

net = ip_network('172.95.116.174/255.255.192.0', 0)

for ip in net:
    # s = f'{ip:b}'
    s  = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 5 == 0:
         print(ip)
         break