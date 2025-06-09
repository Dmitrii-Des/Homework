from ipaddress import ip_address, ip_network

ip = ip_address('127.63.67.1')

for A in range(16, 25):
    net = ip_network(f'{ip}/{A}', False)
    if ip in net.hosts():
        for i in net:
            i = f'{int(i):032b}'
            if not(i[:16].count('1') >= i[16:].count('1')):
                break
        else:
            print(A)
            break
print(int('11110000', 2))