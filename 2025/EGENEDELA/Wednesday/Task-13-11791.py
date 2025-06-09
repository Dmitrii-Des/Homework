from ipaddress import ip_address, ip_network

ip = ip_address('246.51.128.202')

min_A = 0
for A in range(16, 25):
    net = ip_network(f'{ip}/{A}', False)
    if ip in net.hosts():
        proverka = True
        for i in net:
            i = f'{int(i):032b}'
            if i[:16].count('0') > i[16:].count('0'):
                proverka = False
                break
        if proverka:
            min_A = A
            break
print(min_A)
print(int('11111110', 2))
