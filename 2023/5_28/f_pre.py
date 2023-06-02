N, A, B = map(int, input().split())

result = 0

for i in range(1,N+1):
    count = 0
    l = [int(x) for x in list(str(i))]
    for j in l:
        count += j
    if (A <= count) and (count <= B):
        result += i

print(result)