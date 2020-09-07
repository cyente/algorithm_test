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

    cnt = 0
    current_steplist = [beginPos]

    while True:
        if endPos in current_steplist:
            ans.append(cnt)
            break
        else:
            new_current_steplist = []
            for curPos in current_steplist:
                if allPos[curPos] == 2:
                    continue
                allPos[curPos] = 2
                temp = (curPos[0]-1, curPos[1])
                if allPos.has_key(temp) and allPos[temp]==1:
                    new_current_steplist.append(temp)
                temp = (curPos[0], curPos[1] -1)
                if allPos.has_key(temp) and allPos[temp] == 1:
                    new_current_steplist.append(temp)
                temp = (curPos[0] + 1, curPos[1])
                if allPos.has_key(temp) and allPos[temp] == 1:
                    new_current_steplist.append(temp)
                temp = (curPos[0], curPos[1]+1)
                if allPos.has_key(temp) and allPos[temp] == 1:
                    new_current_steplist.append(temp)

            current_steplist = new_current_steplist[:]
            cnt += 1

for a in ans:
    print a