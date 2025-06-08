from itertools import product
from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:8]
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('6') == 1:
        for i in alph[1::2]:
            val = val.replace(i, '1')
        if '16' not in val and '61' not in val:
            cnt += 1
print(cnt)