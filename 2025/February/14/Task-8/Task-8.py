from itertools import product

alph = sorted(set('КАЛЕЙДОСКОП'))[::-1]

for pos, val in enumerate(product(alph, repeat=6), start=0):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'К'\
       and val.count('Й') >= 2 and 'С' not in val and 'Е' not in val:
        print(pos)
        break