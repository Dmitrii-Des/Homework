print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = (not(b <= a)) and (c <= d) or a and b and c and (not d)
                if f:
                    print(a, b, c, d)