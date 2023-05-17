N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]

def rotation(A):
    A_return = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            A_return[i][j] = A[N-1-j][i]
    return A_return

def is_ok(A,B):
    for i in range(N):
        for j in range(N):
            if (A[i][j] == 1) and (B[i][j] != 1):
                return False
    return True
    

for i in range(4):
    if is_ok(A,B):
        print('Yes')
        break
    else:
        A = rotation(A)
        if i == 3:
            print('No')
    