import sys
t = int(sys.stdin.readline().strip())
ans = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    beginPos = (0, 0)
    curPos = beginPos
    allPos = {curPos: 1}
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        direction, ret = int(line[0]), int(line[1])
        if ret != -1:
            if direction == 0:
                curPos = (curPos[0]-1, curPos[1])
            elif direction == 1:
                curPos = (curPos[0]+1, curPos[1])
            elif direction == 2:
                curPos = (curPos[0], curPos[1]-1)
            else:
                curPos = (curPos[0], curPos[1]+1)
            allPos[curPos] = 1
    endPos = curPos
    waitingList = []
    waitingList2 = [beginPos]
    cnt = -1
    findFlag = False
    visited = {}
    while waitingList2:
        waitingList = waitingList2.copy()
        waitingList2 = []
        cnt += 1
        while waitingList:
            curPos = waitingList.pop()
            if curPos in visited:
                continue
            else:
                visited[curPos] = 1
            if curPos == endPos:
                findFlag = True
                ans.append(cnt)
                break
            node = (curPos[0]-1, curPos[1])
            if node in allPos and node not in visited:
                waitingList2.append(node)
            node = (curPos[0] + 1, curPos[1])
            if node in allPos and node not in visited:
                waitingList2.append(node)
            node = (curPos[0], curPos[1]-1)
            if node in allPos and node not in visited:
                waitingList2.append(node)
            node = (curPos[0], curPos[1]+1)
            if node in allPos and node not in visited:
                waitingList2.append(node)
        if findFlag == True:
            break
for i in ans:
    print(i)



'''
3
10
0 1
0 -1
1 1
1 1
1 -1
0 1
2 1
2 -1
3 1
3 1
2
3 1
3 1
8
0 1
0 1
3 1
3 1
1 1
1 1
2 1
0 1
'''