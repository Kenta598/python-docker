N = int(input())
A = str(input())
A = A.replace(' ','')

f = []

for i in range(N):
    first = A.find(str(i+1))
    second = A.find(str(i+1),first+1)
    f.append(second+1)

