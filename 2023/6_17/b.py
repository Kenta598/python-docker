A = list(map(int,input().split()))

result = 0

for i,a in enumerate(A):
    result += a*(2**i)

print(result)