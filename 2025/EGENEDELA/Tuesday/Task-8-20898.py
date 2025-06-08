from itertools import product
from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:9]
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('0') == 1:
        for i in alph[1::2]:
            val = val.replace(i, '1')
        if '10' not in val and '01' not in val:
            cnt += 1

print(cnt)
