from ipaddress import ip_address, ip_network

max_A = 0
for A in range(0, 256)[::-1]:
    ip = ip_address(f'217.109.{A}.94')
    net = ip_network(f'217.109.{A}.0/255.255.254.0', False)
    if ip in net.hosts():
        proverka = True
        for i in net:
            i = f'{int(i):032b}'
            if i[:16].count('0') > i[16:].count('0'):
                proverka = False
                break
        if proverka:
            max_A = A
            break

print(max_A)