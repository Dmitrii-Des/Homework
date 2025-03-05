from functools import lru_cache

@lru_cache()
def f(n):
    if n < 5:
        return 4
    if n > 4:
        return 4 * f(n-4)

for i in range(1, 4445):
    f(i)

print(f(4444)//f(4400))