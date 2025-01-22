print('a b c')
for a in range(2):
    for b in range(2):
        for c in range(2):
            f = (a and (not b)) or c
            if not f or f:
                print(a, b, c)