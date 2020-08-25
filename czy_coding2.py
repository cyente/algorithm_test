
# array = [[10, 20, 30], [30, 40, 20]]
"""
input: 
10, 20, 30
30, 40, 20

output:
1, 2, 3
2, 3, 1

"""
import sys
temp = sys.stdin.readline()
array = []
while len(temp) > 0:
    array.append(map(int, temp.strip().split(",")))
    temp = sys.stdin.readline().strip()

def compress(arr):
    new_arr = []
    if not arr or not arr[0]:
        return arr
    for idx in range(len(arr)):
        for jdx in range(len(arr[0])):
            new_arr.append((arr[idx][jdx], idx, jdx))

    x = [0] * len(arr)
    y = [0] * len(arr[0])

    new_arr.sort(key=lambda x: x[0])
    for _, i, j in new_arr:
        val = max(x[i], y[j]) + 1
        x[i] = val
        y[j] = val
        arr[i][j] = val
    return arr

final_array = compress(array)
for line in final_array:

    print ', '.join(map(str, line))



