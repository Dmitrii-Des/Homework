from itertools import product

ans = []

for v in '0123456789':
    for r in range(3):
        for zv in product('0123456789', repeat=r):
            zv = ''.join(zv)
            for v2 in '0123456789':
                for v3 in '0123456789':
                    num = int('12' + v + '3' + zv + '456' + v2 + v3 + '9')
                    if num <= 10**12 and num % 98591 == 0:
                        ans.append((num, num // 98591))

ans = sorted(ans)

for i in ans:
    print(*i)