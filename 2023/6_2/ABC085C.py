N, Y = map(int,input().split())

def otosidama():
    for a in range(N+1):
        for b in range(N+1):
            c = N - (a + b)
            if c >= 0:
                if (10000*a + 5000*b + 1000*c == Y):
                    return a,b,c
                else:
                    continue
    return -1,-1,-1

result = otosidama()
print("{} {} {}".format(result[0],result[1],result[2]))