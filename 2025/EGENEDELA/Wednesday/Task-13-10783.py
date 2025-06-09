from ipaddress import ip_address, ip_network

ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')
ans = []

for mask in range(10, 31):
    net1 = ip_network(f'{ip1}/{mask}', False)
    net2 = ip_network(f'{ip2}/{mask}', False)
    if net1.network_address == net2.network_address:
        ans.append([net1.num_addresses])
print(min(ans))
