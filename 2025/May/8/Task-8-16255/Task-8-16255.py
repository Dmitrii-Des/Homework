from itertools import product

alph = '012345678'
cnt = 0

for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') >= 1 and int(val[-1]) % 3 != 0:
        for i in '357':
            val = val.replace(i, '1')
        if val[0] != '1':
            cnt += 1
print(cnt)