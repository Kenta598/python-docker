import numpy as np

N = int(input())
A = str(input())
A = A.replace(' ','')

f = []

for i in range(N):
    first = A.find(str(i+1))
    second = A.find(str(i+1),first+1)
    f.append(second+1)

result = np.array(f)
result = result.argsort()
result += 1
result = str(result)
result = result.replace('[','')
result = result.replace(']','')
print(result)