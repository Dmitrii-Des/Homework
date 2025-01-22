from itertools import permutations
graph = 'BC BA AC CD DF FG GE CE ED EF'.split()
matrix = '347 3456 1245 1237 236 25 14'.split()
print(*range(1, 8))
for i in permutations('BACDFGE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(42)