from ipaddress import ip_address, ip_network

ip = ip_address('98.81.154.195')
net = ip_network(f'{ip}/255.252.0.0', False)

print(max(net.hosts()))