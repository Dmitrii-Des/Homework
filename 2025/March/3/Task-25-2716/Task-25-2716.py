def f(num):
    divs = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            divs |= {i, num//i}
    divs = sorted(divs)
    if len(divs) < 3:
        return 0
    return sum(divs[-3:])

cnt = 0

for i in range(1_090_000, 1_200_000):
    S = f(i)
    if S != 0 and S % 2022 == 0 and S != i:
        print(i, S)
        cnt += 1
        if cnt == 5:
            break
