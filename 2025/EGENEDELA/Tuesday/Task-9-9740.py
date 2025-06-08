def f1(nums):
    cnt = [nums.count(i) for i in nums]
    return cnt.count(3) == 3 and cnt.count(1) == 4

def f2(nums):
    nepov = [i for i in nums if nums.count(i) == 1]
    pov = [i for i in nums if nums.count(i) != 1]
    return sum(nepov) // len(nepov) <= max(pov)

with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)
def f1(nums):
    cnt = [nums.count(i) for i in set(nums)]  # используем set
    return cnt.count(3) == 1 and len(cnt) == 5  # 1 число повторяется и 4 различны

def f2(nums):
    nepov = [i for i in set(nums) if nums.count(i) == 1]  # используем set
    pov = [i for i in set(nums) if nums.count(i) == 3]  # повторяющееся
    return len(nepov) > 0 and sum(nepov) / len(nepov) <= pov[0]  # проверка на деление на 0

with open('9_9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt += 1
print(cnt)
