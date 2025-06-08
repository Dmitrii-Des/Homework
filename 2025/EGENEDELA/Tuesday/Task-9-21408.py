def f1(nums):
    pov = [i for i in nums if nums.count(i) == 3]
    nepov = [i for i in nums if nums.count(i) == 1]
    return len(pov) == 6 and len(nepov) == 1


def f2(nums):
    max_pov = max([i for i in nums if nums.count(i) > 1])
    max_nepov = max([i for i in nums if nums.count(i) == 1])
    return max_pov > max_nepov

ans = [7, 7, 7, 2, 2, 2]
print(len(ans))
with open('9_21408.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for i in data:
    if f1(i) and f2(i):
        cnt +=1
print(cnt)
