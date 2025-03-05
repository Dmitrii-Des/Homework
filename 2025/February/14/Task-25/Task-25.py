from fnmatch import fnmatch

for i in range(125670 - 125670 % 7777, 10**10, 7777):
    if i % 2 == 0 and fnmatch(str(i), '12*567?'):
        print(i, i//7777)
