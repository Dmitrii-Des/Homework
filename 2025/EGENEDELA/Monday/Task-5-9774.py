from string import digits, ascii_uppercase

def f(num, sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = f(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += f(((N % 3) * 5), 3)
    R = int(R, 3)
    if R > 133:
        ans.append(R)

print(min(ans))