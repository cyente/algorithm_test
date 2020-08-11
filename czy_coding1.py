# import sys
# n, m = list(map(int, sys.stdin.readline().strip().split(" ")))
# dice_list = []
# for idx in range(m):
#     dice_list.append(list(map(lambda x: x - 1, map(int, sys.stdin.readline().strip().split(" ")))))

with open('input1.txt', 'r') as f:
    n, m = list(map(int, f.readline().strip().split(" ")))
    dice_list = []
    for idx in range(m):
        dice_list.append(list(map(lambda x: x-1, map(int, f.readline().strip().split(" ")))))

# dice_list.append()
parent_list = [-1 for _ in range(n)]
rank = [0 for _ in range(n)]

def find_root(i):
    # if parent_list[i] == -1:
    #     return
    while parent_list[i] == -1:
        parent_list[i] = parent_list[parent_list[i]]
        i = parent_list[i]
    return i

def unit(i, j):
    root_i = find_root(i)
    root_j = find_root(j)
    if root_i == root_j:
        return False
    else:
        parent_list[j] = root_i

        root_j





for idx in range(m):
   node_set[dice_list[idx][1]].append(dice_list[idx][0]) 
   





