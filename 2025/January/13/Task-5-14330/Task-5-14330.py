for N in range(10000, 100000):
    digits = sorted(map(int, str(N)))
    maxsquareddigit = (digits[0] + digits[-1])**2
    minsquareddigit = 1
    for i in digits:
        if i % 2 == 0:
             minsquareddigit *= i
    if maxsquareddigit > minsquareddigit:
        res = str(maxsquareddigit) + str(minsquareddigit)
    else:
        res = str(minsquareddigit) + str(maxsquareddigit)
    if res == '12116':
        print(N)
        break