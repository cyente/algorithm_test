import math
import sys
# f=  open('czy_input1.txt', 'r')
M = int(sys.stdin.readline().strip())

def main(A, B, C, D):
    def f(x):
        return A * x * x + x + B

    def F(n, m):
        def _f(x):
            return A * x * x * x / 3. + 0.5 * x * x + B * x

        return abs(_f(m) - _f(n))

    def find_zeros(x1, x2):

        xx1 = -1. / (2 * A) + math.sqrt(1. / (4 * A * A) - B)
        xx2 = -1. / (2 * A) - math.sqrt(1. / (4 * A * A) - B)

        if xx1 >= x2:
            return xx2
        elif xx2 <= x1:
            return xx1
        else:
            return False

    y1 = f(C)
    y2 = f(D)
    if A == 0:
        if y1 * y2 > 0:
            return abs((y1 + y2) * (D-C) * 0.5)
        else:
            x3 = -B
            return 0.5 * (abs(y1 * (x3 - C)) + abs(y2 * (D - x3)))

    xx =  -1. / (2*A)
    if xx >= C and xx >= D:
        return abs(F(C,D))
    if xx <= C and xx <= D:
        return abs(F(C,D))

    y3 = f(-1. / (2*A))
    if y1 * y3 > 0:
        temp_sum = F(C, -1. / (2*A))
    else:
        tempx = find_zeros(C, xx)
        temp_sum = F(C, tempx) + F(tempx, xx)

    if y2 * y3 > 0:
        temp_sum += F(-1. / (2*A), D)
    else:
        tempx = find_zeros(xx, D)
        temp_sum += F(xx, tempx) + F(tempx, D)

    return temp_sum

for _ in range(M):
    # A, B, C, D = map(int, f.readline().strip().split(' '))
    A, B, C, D = map(int, sys.stdin.readline().strip().split(' '))
    print("%.6f" % main(A, B, C, D))

# f.close()




