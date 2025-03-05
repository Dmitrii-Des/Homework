with open('17.txt') as file:
    data = [int(i) for i in file]

max_50 = max([i for i in data if str(i)[-2:] == '50' ])
ans = []

for i in range(len(data) - 2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]
    summ = a1 + a2 + a3
    u1 = len(str(abs(a1))) == 5
    u2 = len(str(abs(a2))) == 5
    u3 = 10000 <= abs(a3) <= 99999
    f1 = u1 + u2 + u3 == 3
    f2 = a1 != a2 and a2 != a3 and a1 != a3
    f3 = summ <= max_50
    if f1 and f2 and f3:
        ans.append(summ)

print(len(ans), max(ans))