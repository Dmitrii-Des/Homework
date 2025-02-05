from itertools import permutations
alph = 'ХОЧУНАБЮДЖЕТ'
cnt = 0
for val in permutations(alph, 12):
    val = ''.join(val)
    for i in 'ОАЮЕ':
        val = val.replace(i, 'У')
    if 'УУУУУ' not in val:
        cnt += 1
print(cnt)