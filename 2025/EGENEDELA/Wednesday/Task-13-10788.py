from ipaddress import ip_address, ip_network

ip1 = ip_address('201.44.240.33')
ip2 = ip_address('201.44.240.107')
cnt = 0

for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address == net2.network_address:
        proverka = True
        for i in net1:
            i = f'{int(i):032b}'
            if i.count('1') < 5:
                proverka = False
                break
        if proverka:
            cnt += 1
print(cnt)