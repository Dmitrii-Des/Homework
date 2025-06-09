cnt_w = 0
min_x = 0
for x in range(1, 3001):
    num = 4**210 + 4**110 - x
    cnt = 0
    while num:
        if num % 4 == 0:
            cnt += 1
        num //= 4
    if cnt > cnt_w:
        cnt_w = cnt
        min_x = x

print(min_x)