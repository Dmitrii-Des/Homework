from itertools import permutations
graph = 'BD DG GA AF FH HC CB BE DE HE GF'.split()
matrix = '234 157 147 138 268 58 23 456'.split()
print(*range(1, 9))
for i in permutations('DGAFHCBE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
print(4+7)