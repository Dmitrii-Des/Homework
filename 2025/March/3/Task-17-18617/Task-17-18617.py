with open('17_18617.txt') as file:
    data = [int(i) for i in file]

max_ost_3 = max(i for i in data)%3
min_ost_7 = min(i for i in data)%7
ans = []

for i in range(len(data)-1):
    a1, a2 = data[i], data[i+1]
    summ = a1 + a2
    u1 = a1 % 3 == max_ost_3
    u2 = a1 % 7 == min_ost_7
    u3 = a2 % 3 == max_ost_3
    u4 = a2 % 7 == min_ost_7
    f1 = u1 + u3 >= 1
    f2 = u2 + u4 >= 1
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))