ans = []
for N in range(28, 100_000):
    R = bin(N)[2:]
    if sum(map(int, R)) % 2 == 0:
        R = '10' + R[2:] + '0'
    else:
        R = '11' + R[2:] + '1'
    R = int(R, 2)
    ans.append(R)

print(min(ans))