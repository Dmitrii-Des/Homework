with open('17_14260.txt') as file:
    data = [int(i) for i in file]

min_4_od = min(i for i in data if abs(i) == i and len(str(i)) == 4 and str(i)[-1] == str(i)[-2])
ans = []

for i in range(len(data)-2):
    a1, a2, a3 = data[i], data[i+1], data[i+2]
    summ = a1 + a2 + a3
    u1 = len(str(abs(a1))) == 3
    u2 = len(str(abs(a2))) == 3
    u3 = len(str(abs(a3))) == 3
    f1 = u1 + u2 + u3 == 3
    f2 = summ > min_4_od
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))