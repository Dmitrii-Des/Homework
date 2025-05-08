from itertools import product

alph = sorted('ЦАПЛЯ')

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val.count('А') <= 1 and val.count('Ц') == 2 and val.count('Л') == 0:
        print(pos)
        break