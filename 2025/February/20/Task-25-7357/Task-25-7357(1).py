from fnmatch import fnmatch


for i in range(0, 10**10, 53191):
    if fnmatch(str(i),'[2468]136*'):
        if int(str(i)[-1]) % 2 == 1:
            print(i, i//53191)