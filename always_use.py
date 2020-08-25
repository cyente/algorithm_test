def Power(x, e):
    # write code here
    flag = 1
    re = 1
    tmp = x
    if e == 0:
        return 1
    if e < 0:
        flag = 0
        e = abs(e)

    while e > 0:
        if e & 1 == 1:
            re = re * tmp
        e >>= 1
        tmp = tmp * tmp  # 2^6=(2*2)^3
    return re if flag else 1 / re