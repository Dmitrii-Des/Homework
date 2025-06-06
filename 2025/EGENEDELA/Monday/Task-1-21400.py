from itertools import permutations

graph = 'EF FA AB BG GE CE CB CD DF DA'.split()
matrix = '457 567 45 136 123 247 126'.split()

print(*range(1, 8))

for i in permutations('ABGEFDC'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

print(18 + 4)