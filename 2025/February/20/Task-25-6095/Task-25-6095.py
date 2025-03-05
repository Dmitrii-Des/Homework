from itertools import product

ans = []

for r in range(4):
    for zv in product('123456789', repeat=r):
        zv = ''.join(zv)
        for n in range(4):
            for zv2 in product('0123456789', repeat=n):
                zv2 = ''.join(zv2)
                num = int(zv + '15' + zv2 + '7424')
                if num <= 10**8 and num % 111 == 0 and num % 113 != 0 and num % 127 != 0:
                    ans.append((num, num // 111))
                if num <= 10**8 and num % 113 == 0 and num % 111 != 0 and num % 127 != 0:
                    ans.append((num, num // 113))
                if num <= 10**8 and num % 127 == 0 and num % 111 != 0 and num % 113 != 0:
                    ans.append((num, num // 127))

ans = sorted(ans)

for i in ans:
    print(*i)