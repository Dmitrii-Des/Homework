from itertools import product

alph = sorted('ПОБЕДА')
ans = 0

for pos, val in enumerate(product(alph, repeat=6), start=1):
     val = ''.join(val)
     if val[0] == 'О' and pos % 2 == 0:
         cnt1 = 0
         for i in 'ПОБЕДА':
             if val.count(i) == 1:
                 cnt1 += 1
             elif val.count(i) != 1:
                 break
         if cnt1 == 6:
             ans = pos

print(ans)

ans2 = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] == 'О' and pos % 2 == 0 and len(set(val)) == 6:
        ans2 = pos
print(ans2)