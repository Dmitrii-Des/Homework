from itertools import product
from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:7]
cnt = 0

for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        for i in alph[::2]:
            val = val.replace(i, '2')
        if val.count('2') == 2:
            cnt += 1

print(cnt)