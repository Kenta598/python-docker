T = int(input())
N = [int(input()) for _ in range(T)]

for t in range(T):
    for i in range(N[t],0,-1):
        if i.bit_count() == 3:
            print(i)
            break
        elif i == 1:
            print(-1)
        else:
            continue