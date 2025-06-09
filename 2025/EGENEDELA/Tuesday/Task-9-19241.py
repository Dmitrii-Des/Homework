def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(3) == 6 and cnt.count(1) == 1

def f2(nums):
    pov = [i for i in nums if nums.count(i) != 1]
    nepov = [i for i in nums if nums.count(i) == 1]
    return sum(pov) / len(pov) < nepov[0]

with open('9_19241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, val in list(enumerate(data, start=1))[::-1]:
    if f1(val) and f2(val):
        print(pos)
        break
