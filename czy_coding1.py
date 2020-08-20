
import sys
m = int(sys.stdin.readline().strip())
coin_list = map(int, sys.stdin.readline().strip().split(' '))

# with open('czy_input1.txt', 'r') as f:
#     m = int(f.readline().strip())
#     coin_list = map(int, f.readline().strip().split(' '))

def share(coin_list):
    if len(coin_list) <= 1:
        return  -1

    coin_list.sort()
    sum_ = sum(coin_list)
    half = sum_ / 2.
    coin_list = coin_list[::-1]

    dp = [[0 for _ in range(int(half))]for _ in range(m)]
    for idx in range(m+1):
        for jdx in range(int(half+1)):
            if jdx - coin_list[idx] >= 0:
                dp[idx][jdx] = max([dp[idx-1][jdx],
                                    dp[idx-1][jdx - coin_list[idx]]+coin_list[idx]
                                    ])
            else:
                dp[idx][jdx] = dp[idx-1][jdx]

    x1 = dp[-1][-1]
    x2 = sum_ - x1
    return abs(x1 - x2)


print share(coin_list)





















