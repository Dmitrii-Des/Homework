from string import digits, ascii_uppercase
from itertools import product

alph = (digits + ascii_uppercase)[:15]
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and len([j for j in val if j in ascii_uppercase]) >= 2:
        cnt += 1

print(cnt)