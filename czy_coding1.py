
import sys
m = int(sys.stdin.readline().strip())
coin_list = map(int, sys.stdin.readline().strip().split(' '))

# with open('input1.txt', 'r') as f:
#     m = int(f.readline().strip())
#     coin_list = map(int, f.readline().strip().split(' '))

def share(coin_list):
    if len(coin_list) <= 1:
        return  -1


    coin_list.sort()
    sum_ = sum(coin_list)
    half = sum_ / 2.
    coin_list = coin_list[::-1]
    x1 = 0
    x2 = 0
    for coin in coin_list:
        if x1 + coin <= half:
            x1 += coin
        elif x2 + coin <= half:
            x2 += coin
        else:
            print("some thing wrong")
    return abs(x1 - x2)


print share(coin_list)





















