A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            place = 500*a + 100*b + 50*c
            if place != X:
                continue
            else:
                count += 1
                continue

print(count)