def f(num):
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs |= {i, num//i}
    if len(divs) < 2:
        return 0
    return min(divs) + max(divs)

cnt = 0

for i in range(220_001, 10**20):
    M = f(i)
    if M % 10 == 4:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break