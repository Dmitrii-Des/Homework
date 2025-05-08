def dell(n, m):
    return n % m == 0

def f(A):
    for x in range(1, 1000):
        u = dell(A, 12) and (dell(530, x) <= ((not dell(A, x)) <= (not dell(170, x))))
        if not u:
            return False
    return True

cnt = 0

for A in range(1, 1001):
    if f(A):
        cnt += 1
print(cnt)