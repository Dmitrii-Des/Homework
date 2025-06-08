def f1(nums):
    nums = [i for i in nums]
    return nums == sorted(nums)[::-1]
def f2(nums):
    nums = [i for i in nums]
    return (max(nums)+min(nums)) // 2 > (sum(nums)-max(nums)-min(nums)) // 5


with open('9_21704.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, val in enumerate(data, start=1):
    if f1(val) and f2(val):
        print(sum(val))
        break