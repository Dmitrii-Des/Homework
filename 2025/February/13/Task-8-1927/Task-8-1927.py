from itertools import product
alph = sorted('ЯСНОВИДЕЦ')
cnt = 0
for val in product(alph, repeat = 5):
    val = ''.join(val)
    if val.count(val[0]) == 1 and val.count(val[-1]) == 1:
        for i in 'СНВДЦ':
            val = val.replace(i, 'М')
        for j in 'ЯОИЕ':
            val = val.replace(j, 'У')
        if val[0] == 'М' and val[-1] == 'У':
            cnt += 1
print(cnt)