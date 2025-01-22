from itertools import product
from string import digits, ascii_uppercase
alph = (digits + ascii_uppercase)[:16]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('6') == 2 and val[0] != '0':
        for chet in '0248ACE':
            val = val.replace(chet, 'K')
        if 'K6' not in val and '6K' not in val and '66' not in val:
            cnt += 1
print(cnt)