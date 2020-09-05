
def cha(number, arr):
    sum_arr = sum(arr)
    lenght = len(arr)

    dp = [[0 for i in range(sum_arr)] for j in range(lenght+1)]

    for i in range(1, lenght+1):
        for j in range(1, sum_arr//2+1):
            if j >= arr[i-1]:
                #print(i, j, arr[i-1])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - arr[i - 1]] +
                               arr[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return sum_arr - 2*dp[lenght][sum_arr//2]

#mm = cha(5, [5, 10, 8, 2, 10])
mm = cha(3, [1,2,3])
print(mm)
print('test')