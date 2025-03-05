from itertools import product

ans = []

for r in range(6):
    for zv in product('02468', repeat=r):
        zv1 = ''.join(zv)
        if not zv1.startswith('0'):  # if len(zv1) == 0 or zv1[0] != '0':
            for v in '13579':
                for v2 in '13579':
                    num = int(zv1 + '12' + v + '4' + v2)
                    if num % 9231 == 0:
                        ans.append((num, num // 9231))

ans = sorted(ans)

for i in ans:
    print(*i)