from ipaddress import ip_address, ip_network

net = ip_network('218.194.82.148/255.255.255.192', False)
cnt = 0

print(max(net.hosts()))