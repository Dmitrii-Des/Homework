def f(num):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = f(N)
    ost = f((N % 3) * 5)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += ost
    R = int(R, 3)
    if R > 133:
        ans.append(R)
print(min(ans))