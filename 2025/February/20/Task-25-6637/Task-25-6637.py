from itertools import product

ans = []

for r in range(4):
    for zv in product('0123456789', repeat=r):
        zv = ''.join(zv)
        for v in '0123456789':
            num = int('1' + v + '2139' + zv + '4')
            if num <= 10**10 and num % 3052 == 0:
                ans.append((num, num // 3052))

ans = sorted(ans)

for i in ans:
    print(*i)