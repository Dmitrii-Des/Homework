from string import digits, ascii_uppercase

def f(num, sys):
    alph = digits + ascii_uppercase
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for N in range(3, 100_000)[::-1]:
    R = f(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + f(((N % 3) * 3), 3)
    R = int(R, 3)
    if R <= 150:
        print(N)
        break