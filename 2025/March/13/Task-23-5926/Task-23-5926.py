ans = set()
def f(cur, action, cnt):
    if cnt == 24:
        ans.add(cur)
        return 1
    if action == '':
        return f(cur + 1, '+1', cnt + 1) + f(cur + 7, '+7', cnt + 1) + f(cur * 4, '*4', cnt + 1)
    if action == '+1':
        return f(cur + 7, '+7', cnt + 1) + f(cur * 4, '*4', cnt + 1)
    if action == '+7':
        return f(cur + 1, '+1', cnt + 1) + f(cur * 4, '*4', cnt + 1)
    if action == '*4':
        return  f(cur + 7, '+7', cnt + 1) + f(cur + 1, '+1', cnt + 1)

f(1, '', 0)
print(len(ans))