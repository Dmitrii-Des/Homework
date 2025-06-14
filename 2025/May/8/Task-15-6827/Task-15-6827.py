from itertools import permutations, combinations


def f(x):
    A = A1 <= x <= A2
    R = 99 <= x <= 258
    P = 257 <= x <= 1000
    Q = 5 <= x <= 100
    return (A <= R) and ((not(A <= P)) <= Q)

ans = []
line = [x/10 for x in range(4*10, 1001*10)]

for A1, A2 in combinations(line , 2):
    if all(f(x) for x in line):
        ans.append(A2-A1)
print(min(ans))