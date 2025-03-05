def f(x):
        return (not (x & 79 == 0)) and ((x & 31 == 0) <= (not (x & A == 0)))


ans = []

for A in range(0, 100_000):
    if all(f(x) for x in range(90, 101)):
        ans.append(A)

print(min(ans))