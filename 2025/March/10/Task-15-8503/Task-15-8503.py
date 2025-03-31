def f(A):
    for x in range(0, 1_000):
        u = ((x & 52 != 0) and (x & 36 == 0)) <= (not(x & A == 0))
        if not u:
            return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)
        break