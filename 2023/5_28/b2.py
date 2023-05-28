T = int(input())
N = [int(input()) for _ in range(T)]

for t in range(T):
    for i in range(N[t],0,-1):
        count = bin(i).count('1')
        if count == 3:
            print(i)
            break
        elif i == 1:
            print(-1)
        else:
            continue
