from fnmatch import fnmatch

def f(num):
    divs = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divs |= {i, num//i}
    return divs

cnt = 0
for i in range(69750, 10**10):
    divs_chet = [x for x in f(i) if x % 2 == 0]
    if len(divs_chet) >= 4 and fnmatch(str(i), '6*97*5?'):
        print(i, sum(divs_chet))
        cnt += 1
        if cnt == 7:
            break
