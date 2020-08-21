
import sys
m = int(sys.stdin.readline().strip())
coin_list = map(int, sys.stdin.readline().strip().split(' '))

# with open('czy_input1.txt', 'r') as f:
#     m = int(f.readline().strip())
#     coin_list = map(int, f.readline().strip().split(' '))

def cha(number, arr):
    if len(arr) == 1:
        return -1
    sum_arr = sum(arr)
    lenght = len(arr)

    dp = [[0 for i in range(sum_arr)] for j in range(lenght+1)]

    for i in range(1, lenght+1):
        for j in range(1, sum_arr//2+1):
            if j >= arr[i-1]:
                #print(i, j, arr[i-1])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1]] + arr[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return sum_arr - 2*dp[lenght][sum_arr//2]

#mm = cha(5, [5, 10, 8, 2, 10])
mm = cha(m, coin_list)
print(mm)
