from itertools import permutations
alph = 'ХОЧУ В ВУЗ'
cnt = 0
for val in set(permutations(alph, 10)):
    val = ''.join(val)
    if val[0] != ' ' and val[-1] != ' ' and '  ' not in val:
        val = val.split()
        if val[0][0] != 'У' and val[1][0] != 'У' and val[2][0] != 'У':
            cnt += 1
print(cnt-1) #ХОЧУ В ВУЗ не учитываем