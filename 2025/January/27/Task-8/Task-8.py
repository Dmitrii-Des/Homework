from itertools import product
alph = '0123456789AB'
cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val.count('B') == 2 and val[0] != '0':
        for i in '02468A':
            val = val.replace(i, 'G')
        for p in '13579B':
            val = val.replace(p, 'L')
        if 'GG' not in val and 'LL' not in val:
            cnt += 1
print(cnt)