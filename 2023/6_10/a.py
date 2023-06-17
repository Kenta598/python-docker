N = int(input())

front = N
back = N
result = 0

for i in range(5):
    if N%5 == 0:
        result = N
        break
    front += 1
    back -= 1
    if front%5 == 0:
        result = front
        break
    elif back%5 == 0:
        result = back
        break

print(result)