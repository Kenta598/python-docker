import itertools

N = int(input())
A = list(map(int,input().split()))

ls = list(itertools.permutations(A))

length = len(ls)
length_i = N//2

flag = False

for n in range(length):
    for j in range(length_i):
        i = 2 + 2*j - 1
        if (ls[n][i-1] >= ls[n][i]) or (ls[n][i] <= ls[n][i+1]):
            break
        else:
            if i != N-2:
                continue
            else:
                flag = True
                break

print("Yes" if flag else "No")