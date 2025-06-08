def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(2) == 4 and cnt.count(1) == 3

def f2(nums):
    nums = [i for i in nums]
    pov = [i for i in nums if nums.count(i) != 1]
    return max(nums) not in pov

with open('9_9832.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, val in enumerate(data, start=1):
    if f1(val) and f2(val):
        print(sum(val))
        break
