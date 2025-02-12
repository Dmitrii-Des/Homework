with open('17_19249.txt') as file:
    data = [int(i) for i in file]
    maxkv_43 = max([i for i in data if len(str(abs(i))) == 5 and str(i)[-2:] == '43'])**2
ans = []
for i in range(len(data) - 2):
    a1, a2, a3 = data[i], data[i + 1], data[i + 2]
    summ_kv = a1**2+a2**2+a3**2
    u1 = (len(str(abs(a1))) == 5) and (str(abs(a1))[-2:] == '43')
    u2 = 10000 <= abs(a2) <= 99999 and (str(abs(a2))[-2:] == '43')
    u3 = 10000 <= abs(a3) <= 99999 and (str(abs(a3))[-2:] == '43')
    f1 = u1 + u2 + u3 >= 1
    f2 = summ_kv <= maxkv_43
    if f1 and f2:
        ans.append(summ_kv)
print(len(ans), min(ans))