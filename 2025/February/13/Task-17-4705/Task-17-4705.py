with open('17_4705.txt') as file:
    data = [int(i) for i in file]
maxkv_3 = max([i for i in data if str(abs(i))[-1] == '3'])**2
ans = []
for i in range(len(data) - 1):
    a1, a2 = data[i], data[i+1]
    summkv = a1**2 + a2**2
    u1 = str(abs(a1))[-1] == '3'
    u2 = str(abs(a2))[-1] == '3'
    f1 = u1 + u2 == 1
    f2 = summkv >= maxkv_3
    if f1 and f2:
        ans.append(summkv)
print(len(ans), max(ans))