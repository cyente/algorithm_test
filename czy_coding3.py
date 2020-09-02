
# array = [[1, 1, 1, 4], [1, 2, 3, 4]]
"""
input:
1, 1, 1, 4
1, 2, 3, 4

output:
1, 1, 1, 4
1, 2, 3, 4

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
    min_x = [10 ** 9] * len(arr)
    min_y = [10 ** 9] * len(arr[0])
    lastval = 10 ** 9
    new_arr.sort(key=lambda x: x[0])
    for curr_val, i, j in new_arr:
        if curr_val == min_x[i] or curr_val == min_y[j]:
            valx = x[i] if curr_val == min_x[i] else x[i] + 1
            valy = y[j] if curr_val == min_y[j] else y[j] + 1
            val = max(valx, valy)
        else:
            val = max(x[i], y[j]) + 1
        x[i] = val
        y[j] = val
        min_x[i] = curr_val
        min_y[i] = curr_val
        arr[i][j] = val
        if lastval != curr_val:
            lastval = curr_val
            dicx, dicy = {}, {}
            dicx[i] = [(i, j)]
            dicy[j] = [(i, j)]
        else:
            if not dicx.has_key(i):
                dicx[i] = [(i, j)]
            else:
                dicx[i].append((i, j))
            if not dicy.has_key(j):
                dicy[j] = [(i, j)]
            else:
                dicy[j].append((i, j))
            samePoints = [(i, j)]
            while samePoints:
                x0, y0 = samePoints.pop()
                if dicx.has_key(x0):
                    for x1, y1 in dicx[x0]:
                        if arr[x1][y1] != val:
                            arr[x1][y1] = val
                            samePoints.append((x1, y1))
                if dicy.has_key(y0):
                    for x1, y1 in dicy[y0]:
                        if arr[x1][y1] != val:
                            arr[x1][y1] = val
                            samePoints.append((x1, y1))

    return arr

final_array = compress(array)
for line in final_array:

    print ', '.join(map(str, line))



