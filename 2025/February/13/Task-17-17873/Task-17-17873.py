with open('17_17873.txt') as file:
    data = [int(i) for i in file]
minn = min([i for i in data])
ans = []
for i in range(len(data) - 1):
    a1, a2 = data[i], data[i + 1]
    u1 = a1 % 16 == minn
    u2 = a2 % 16 == minn
    f = u1 + u2 >= 1
    if f:
        ans.append(a1+a2)
print(len(ans), max(ans))