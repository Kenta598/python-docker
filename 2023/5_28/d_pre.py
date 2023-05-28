N = int(input())
A = list(map(int,input().split()))

def replace(A,N):
    count = 0
    flag = True
    while(True):
        for i in range(N):
            if (i == N-1) and (A[i]%2 == 0):
                count += 1
            elif (A[i] % 2 == 0):
                continue
            else:
                flag = False
                break
        if flag:
            A = list(map(lambda x:x/2,A))
            continue
        else:
            break
    return count

print(replace(A,N))