N = int(input())
A = list(map(int,input().split()))
Q = int(input())
lr = [list(map(int,input().split())) for _ in range(Q)]

def start_finish(lr):
    for i in range(0,N-1,1):
        if A[i] <= lr and lr <= A[i+1]:
            return i
        else:
            continue

sleep = 0
flag = False

for j in range(Q):
    ind_start = start_finish(lr[j][0])
    ind_finish = start_finish(lr[j][1])
    for i in range(N):
        if i%2 == 0:
            continue
        else:
            if ind_start == i:
                sleep += A[i+1] - lr[j][0]
            elif ind_finish == i:
                sleep += lr[j][1] - A[i]
            elif ind_start < i and i < ind_finish:
                sleep += A[i+1] - A[i]
            else:
                continue
    print(int(sleep))
    sleep = 0