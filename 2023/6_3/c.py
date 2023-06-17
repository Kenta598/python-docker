import math

N, D = map(int,input().split())
XY = [list(map(int,input().split())) for _ in range(N)]

flag = []
for i in range(N):
    if i == 0:
        flag.append(True)
    else:
        flag.append(False)

flag_pre = []
for i in range(N):
    if i == 0:
        flag.append(True)
    else:
        flag.append(False)

def distance(pre,next):
    return math.sqrt(math.pow(next[0] - pre[0],2) + math.pow(next[1] - pre[1],2))

def check(pre,flag):
    for j in range(N):
        dis = distance(pre,XY[j])
        if dis <= D:
            flag[j] = True
        else:
            continue

while(True):
    for i in range(N):
        if flag[i]:
            check(XY[i],flag)
        else:
            continue
    if flag_pre != flag:
        flag_pre = flag
        continue
    else:
        break

for i in range(N):
    if flag[i]:
        print('Yes')
    else:
        print('No')