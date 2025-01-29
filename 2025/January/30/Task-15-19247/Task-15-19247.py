def f(A):
    for x in range(1, 1_000):
        for y in range(1, 1_000):
            u = (x - 3*y < A) or (y > 400) or (x > 56)
            if not u:
                return False
    return True
for A in range(0, 10_000):
    if f(A):
        print(A)
        break