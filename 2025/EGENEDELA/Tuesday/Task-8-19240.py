from itertools import product

alph = sorted('ЯНВАРЬ')
ans = 0

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] != 'Я' and val.count('Ь') <= 1 and 'ЯЯ' not in val:
        ans = pos
print(ans)