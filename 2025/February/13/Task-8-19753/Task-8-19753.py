from itertools import product
alph = '0123456789'
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val[0] != '0' and int(val) % 4 == 0:
        if val.count('0') <= 1 and val.count('1') <= 1 and val.count('2') <= 1 and val.count('3') <= 1 and val.count('4') <= 1\
           and val.count('5') <= 1 and val.count('6') <= 1 and val.count('7') <= 1 and val.count('8') <= 1 and val.count('9') <= 1:
            for i in '02468':
                val = val.replace(i, '2')
            if '22' not in val:
                cnt += 1
print(cnt)