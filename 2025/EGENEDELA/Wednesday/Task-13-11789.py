from ipaddress import ip_address, ip_network

ip = ip_address('99.8.254.232')
min_A = 0

for A in range(16, 25):
    net = ip_network(f'{ip}/{A}', False)
    if ip in net.hosts():
        proverka = True
        for i in net:
            i = f'{int(i):032b}'
            if i[:16].count('1') > i[16:].count('1'):
                proverka = False
                break
        if proverka:
            min_A = A
            break
print(min_A)
print(int('11111000', 2))