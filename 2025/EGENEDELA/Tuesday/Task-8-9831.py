from itertools import product
from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:16]
cnt = 0

for val in product(alph, repeat=3):
    val = ''.join(val)
    if len(set(val)) == 3 and val[0] != '0':
        for i in alph[::2]:
            val = val.replace(i, '2')
        for i in alph[1::2]:
            val = val.replace(i, '1')
        if '12' not in val and '21' not in val:
            cnt += 1
print(cnt)