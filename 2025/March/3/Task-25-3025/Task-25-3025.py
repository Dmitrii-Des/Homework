def f(num):
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs |= {i, num//i}
    return sorted(divs)

cnt = 0

for i in range(200_000_001, 10**20):
    D = [i for i in f(i) if i % 2 != 0]
    if len(D) >= 6:
        print(i, D[-6])
        cnt += 1
        if cnt == 5:
            break


