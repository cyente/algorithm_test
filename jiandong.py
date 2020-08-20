
import sys
m = int(sys.stdin.readline().strip())
coin_list = map(int, sys.stdin.readline().strip().split(' '))


def cha(number, arr):
    sum_arr = sum(arr)
    lenght = len(arr)
    if len(arr) == 1:
        return -1
    dp = [0 for i in range(sum_arr)]
    judge = sum_arr//2+1
    for i in range(1, lenght+1):
        for jdx in range(judge):
            j = judge - jdx
            if j >= arr[i-1]:
                #print(i, j, arr[i-1])
                dp[j] = max(dp[j],
                            dp[j - arr[i - 1]] + arr[i-1]
                            )
            else:
                dp[j] = dp[j]

    return abs(sum_arr - 2*dp[judge -1])

#mm = cha(5, [5, 10, 8, 2, 10])
mm = cha(m, coin_list)
print(mm)
