from itertools import product
from string import digits, ascii_uppercase

alph = (digits + ascii_uppercase)[:9]
cnt = 0

for val in product(alph, repeat=5):
    val = ''.join(val)
    if val.count('5') == 1 and val[0] != '0' and all([val[i] != val[i + 1] for i in range(4)]):
            cnt += 1
print(cnt)