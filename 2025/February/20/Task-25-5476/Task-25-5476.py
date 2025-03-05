from itertools import product

ans = []

for v in '123456':
    for r in range(4):
        for zv in product('0123456', repeat=r):
            zv = ''.join(zv)
            num = int(v + '213' + zv + '5664', 7)
            if num <= 10 ** 9 and num % 333 == 0:
                ans.append((num, num // 333))

ans = sorted(ans)

for i in ans:
    print(*i)