from itertools import product

ans = []

for r in range(7):
    for zv in product('0123456789', repeat=r):
        zv = ''.join(zv)
        if zv == '' or int(zv) % 2 == 1:
            for v in '2468':
                num = int(v + '136' + zv)
                if num <= 10**10 and num % 53191 == 0:
                    ans.append((num, num // 53191))

ans = sorted(ans, key=lambda x: x[0], reverse=True)[:5] #Можно без key=lambda x: x[0], так как изначально\
# функция сортирует так

for i in ans:
    print(*i)