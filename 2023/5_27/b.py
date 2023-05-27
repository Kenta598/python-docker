N, M = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(M)]

def make_frindlist(N,M,a):
    friend = []
    for m in range(M):
        for n in range(N):
            if (n + 1 < N):
                friend.append([a[m][n],a[m][n+1]])
            if (n - 1 >= 0):
                friend.append([a[m][n],a[m][n-1]])
            else:
                continue
    return friend

friend = make_frindlist(N,M,a)

pair = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if i != j:
            pair.append([i,j])

not_friend = [i for i in pair if i not in friend]
print(not_friend)
print(int(len(not_friend)/2))