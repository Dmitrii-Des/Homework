def f(num):
    res = ''
    while num:
        res += str(num % 4)
        num //= 4
    return res[::-1]


ans = []

for N in range(1, 100_000):
    R = f(N)
    if len(R) % 2 == 0:
        R = R[:len(R) // 2] + '0' + R[len(R) // 2:]
    else:
        R = R
    R = int(R)

    if R <= 180:
        ans.append(N)
print(max(ans))