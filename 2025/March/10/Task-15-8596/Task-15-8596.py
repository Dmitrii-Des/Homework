def f(A):
    for x in range(0, 1_000):
        for y in range(0, 1_000):
            u = (x >= 11) or (3 * x < y) or (x * y < A)
            if not u:
                return False
    return True
for A in range(0, 1_000):
    if f(A):
        print(A)
        break