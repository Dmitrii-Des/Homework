def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(2) == 2 and cnt.count(1) == 4
def f2(nums):
    pov_1 = [i for i in nums if nums.count(i) !=1][0]
    nepov = [i for i in nums if nums.count(i) == 1]
    return pov_1 >= sum(nepov) // len(nepov)

with open('09_9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, val in enumerate(data, start=1):
    if f1(val) and f2(val):
        print(pos)
        break