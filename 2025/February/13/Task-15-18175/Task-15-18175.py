def dell(n, m):
    return n % m == 0
def f(A):
    for x in range(1, 1000):
        u = ((not dell(x, 7)) and dell(x, 13)) <= (x > A - 40)
        if not u:
            return False
    return True
for A in range(1, 1000)[::-1]:
    if f(A):
        print(A)
        break