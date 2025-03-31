from fnmatch import fnmatch

def f(num):
    divs = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divs |= {i, num // i}
    return [x for x in divs if fnmatch(str(x), '*7?')]

for i in range(400_000, 500_001):
    if len(f(i)) >= 18:
        print(i, sum(f(i)))
