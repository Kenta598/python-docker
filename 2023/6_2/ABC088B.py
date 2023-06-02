N = int(input())
a = list(map(int,input().split()))

alice = 0
bob = 0

def max(ls):
    max = -1
    ind = 0
    return_ind = -1
    for i in ls:
        if i > max:
            max = i
            return_ind = ind
        ind += 1
    return ls.pop(return_ind)

for i in range(N):
    if i%2 == 0:
        alice += int(max(a))
    else:
        bob += int(max(a))

print(alice-bob)