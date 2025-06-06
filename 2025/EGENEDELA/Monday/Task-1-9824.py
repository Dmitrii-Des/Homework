from itertools import permutations

graph = 'AB BC CE EG DF FA ED CA'.split()
matrix = '346 45 16 125 247 137 56'.split()

print(*range(1, 8))

for i in permutations('ABCEGDF'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)