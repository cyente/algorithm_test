
# import sys
# n,m  = map(int, sys.stdin.readline().strip().split(" "))
# x = [0 for _ in range(n)]
# numsc = [[]for _ in range(n)]
# for idx in range(n):
#     temp = map(int, sys.stdin.readline().strip().split(" "))
#     x[idx] = temp[0]
#     numsc[idx] = temp[1:]

with open('input1.txt', 'r') as f:
    n, m = map(int, f.readline().strip().split(" "))
    x = [0 for _ in range(n)]
    numsc = [[] for _ in range(n)]
    for idx in range(n):
        temp = map(int, f.readline().strip().split(" "))
        x[idx] = temp[0]
        numsc[idx] = temp[1:]

max_output = 0
recent_list = []

for idx in range(n):
    if len(numsc[idx]) >= 2:
        recent_list.append([numsc[idx][0], idx, 0])
        recent_list.append([numsc[idx][-1], idx, -1])
    elif len(numsc[idx]) == 1:
        recent_list.append([numsc[idx][0], idx, 0])



def dfs(k, now_val, max_output):
    if k == m:
        if max_output < now_val:
            max_output = now_val
            return max_output

    for idx in range(n):
        if len(numsc[idx]) >= 2:
            for choose in range(2):
                cval = numsc[idx][choose-1]
                numsc[idx].pop(choose-1)
                max_output = dfs(k + 1, now_val + cval, max_output)
                numsc[idx].insert(choose - 1, cval)
        if len(numsc[idx]) >= 1:
            choose = 0
            cval = numsc[idx][choose - 1]
            numsc[idx].pop(choose - 1)
            max_output = dfs(k + 1, now_val + cval, max_output)
            numsc[idx].insert(choose - 1, cval)

    return max_output

print dfs(0, 0, 0)
















