for N in range(1, 100_000)[::-1]:
    R = bin(N)[2:]
    if N % 2 == 0:
        R += R[-2:]
    else:
        R = '1' + R + '0'
    R = int(R, 2)
    if R < 100:
        print(N)
        break