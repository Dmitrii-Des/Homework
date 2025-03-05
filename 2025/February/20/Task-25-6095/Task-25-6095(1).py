from fnmatch import fnmatch

for i in range(10**8):
    ost = [i % 111 == 0, i % 113 == 0, i % 127 == 0]
    if sum(ost) == 1 and fnmatch(str(i), '*15*7424'):
        print(i, i//111 if ost[0] == 1 else i // 113 if ost[1] == 1\
              else i // 127)