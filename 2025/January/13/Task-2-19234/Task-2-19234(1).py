print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not(((not x) or y) and (not w))) or (not(z and (not(y and w))))
                if not f:
                    print(x, y, z, w)