from ipaddress import ip_address, ip_network

net = ip_network('192.168.32.48/255.255.255.240')
cnt = 0

for i in net:
    i = f'{int(i):032b}'
    if i.count('1') % 2 != 0:
        cnt += 1

print(cnt)