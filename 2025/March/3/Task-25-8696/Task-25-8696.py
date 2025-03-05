def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs |= {i, num//i}
    divs = sorted(divs)
    if is_prime(num):
        return 0
    return sum(map(int, divs))

cnt = 0
for i in range(1_273_547, 10**20):
    M = f(i)
    if is_prime(M % 100_000) and M != 0:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break