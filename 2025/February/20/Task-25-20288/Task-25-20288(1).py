from re import fullmatch

for i in range(12040 - 12040 % 9231, 10**10, 9231):
    if fullmatch(r'[02468]*12[13579]4[13579]', str(i)):
        print(i, i//9231)