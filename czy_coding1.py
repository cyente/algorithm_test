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



