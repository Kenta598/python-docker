N = int(input())
d = list(int(input()) for _ in range(N))

def max(ls):
    max = -1
    return_ind = 0
    for i,r in enumerate(ls):
        if max <= r:
            max = r
            return_ind = i
    return ls.pop(return_ind)

base = 101
step = 0

for i in range(N):
    candidate = max(d)
    if base > candidate:
        base = candidate
        step += 1
print(step)