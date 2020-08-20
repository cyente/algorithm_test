n=int(input().strip())
arr=list(map(int,input().split()))
def split_array(a):
    a.sort()
    print(a)
    b = []
    # 以上a,b作为待返回的数组
    # 计算数组大小
    n = len(a)#1000
    #求和
    smr = sum(a)
    # 和的一半,简称半和
    hs = smr / 2
    # 临时和
    s = 0
   # 从最大的数字开始遍历数组
    for i in range(n-1,-1,-1):
        # 预判该数字加和结果
        ns = s + a[i]
        if ns > hs:
            # 如果超出半和则跳过
            continue
        else:
            # 如果未超过半和,则:
            # 1, 取该元素加和
            s += a[i]
            # 2, 从 a 中将元素转移到 b
            b.append(a[i])
            a.pop(i)
            # 如果最终和与半和之差,不够最小元素,则完成
            if abs(s - hs) <= a[0]:
                break
    return abs(sum(a)-sum(b))

if n<=1:
    print(-1)
else:
    print(split_array(arr))