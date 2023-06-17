N = int(input())
SA = list(input().split() for _ in range(N))

S = []
A = []

for i in SA:
    S.append(i[0])
for i in SA:
    A.append(int(i[1]))

def min(ls):
    min = 1000000009
    ind = -1
    for i,age in enumerate(ls):
        if min > age:
            min = age
            ind = i
    return ind

start = min(A)
ind = min(A)
for i in range(N):
    if ind < N:
        print(S[ind])
        ind += 1
    elif ind == N:
        print(S[0])
        ind = 1
        continue
    elif ind == start:
        print(S[ind])
        break