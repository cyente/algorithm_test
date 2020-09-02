# import sys

# with open('czy_input.txt', 'r') as f:
#     K = int(f.readline().strip())
#     N = int(f.readline().strip())
#     W_list = list(map(int, f.readline().strip().split(' ')))
#     V_list = list(map(int, f.readline().strip().split(' ')))


import sys
K = int(sys.stdin.readline().strip())

N = int(sys.stdin.readline().strip())
W_list = list(map(int, sys.stdin.readline().strip().split(' ')))
V_list = list(map(int, sys.stdin.readline().strip().split(' ')))


def package(K, N, W_list, V_list):

    dp = [0 for i in range(K + 1)]

    for i in range(N):
        for j in range(K, -1, -1):
            if j >= W_list[i]:
                dp[j] = max(dp[j], dp[j - W_list[i]] + V_list[i])
    return dp[-1]

print package(K, N, W_list, V_list)
