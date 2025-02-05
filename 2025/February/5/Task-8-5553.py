from itertools import permutations
alph = 'СОТОЧКА'
cnt = 0
for val in set(permutations(alph, 7)):
    val = ''.join(val)
    if 'ОО' in val or 'АА' in val or 'АО' in val or 'ОА' in val:
        cnt += 1
print(cnt)