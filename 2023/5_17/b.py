n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

max_t = -1
max_0 = -1

for i in range(n):
    if c[i]  == t:
        if max_t < r[i]:
            max_t = r[i]
            ans_t = i + 1
    if c[i] == c[0]:
        if max_0 < r[i]:
            max_0 = r[i]
            ans_0 = i + 1

print(ans_t if max_t != -1 else ans_0)