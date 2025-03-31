def f(cur, end, a, b):
    if abs(cur) > 33: return 0
    if len(b) != len(a): return 0
    if cur == end: return 1
    return f(cur + 2, end, a | {cur + 2}, b + [cur + 2]) + f(cur - 3, end, a | {cur - 3}, b + [cur - 3])


print(f(1, 30, set([1]), [1]))