def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(2) == 6 and cnt.count(1) == 1

def f2(nums):
    pov = [i for i in nums if nums.count(i) != 1]
    nepov = [i for i in nums if nums.count(i) == 1]
    return (max(pov) + min(pov)) // 2 < nepov[0]

with open('9_12241.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)