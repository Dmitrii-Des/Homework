def f1(nums):
    nums = [i for i in nums]
    return max(nums) + min(nums) <= sum(nums) - max(nums) - min(nums)
with open('9_17628.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i):
        cnt += 1
print(cnt)