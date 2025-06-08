from itertools import product
from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:9]
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') <= 1 and val[-1] not in '18' and val[0] not in '1357':
        cnt += 1
print(cnt)